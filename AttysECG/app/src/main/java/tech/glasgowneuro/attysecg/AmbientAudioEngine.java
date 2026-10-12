package tech.glasgowneuro.attysecg;

import android.content.Context;
import android.content.res.AssetManager;
import android.util.Log;

public class AmbientAudioEngine {

    private static final String TAG = "AmbientAudioEngine";

    static {
        try {
            System.loadLibrary("attysecg_audio");
        } catch (UnsatisfiedLinkError e) {
            Log.e(TAG, "Could not load attysecg_audio native library", e);
        }
    }

    private native void nativeInit(AssetManager assetManager);
    private native void nativeStart();
    private native void nativeStop();
    private native void nativeSendHR(float hr);

    private boolean isRunning = false;

    public AmbientAudioEngine(Context context) {
        try {
            nativeInit(context.getAssets());
        } catch (Exception e) {
            Log.e(TAG, "Failed to initialize ambient audio engine", e);
        }
    }

    public synchronized void start() {
        if (!isRunning) {
            try {
                nativeStart();
                isRunning = true;
            } catch (Exception e) {
                Log.e(TAG, "Failed to start ambient audio engine", e);
            }
        }
    }

    public synchronized void stop() {
        if (isRunning) {
            try {
                nativeStop();
                isRunning = false;
            } catch (Exception e) {
                Log.e(TAG, "Failed to stop ambient audio engine", e);
            }
        }
    }

    public void sendHR(float hr) {
        if (isRunning) {
            try {
                nativeSendHR(hr);
            } catch (Exception e) {
                Log.e(TAG, "Failed to send HR to ambient audio engine", e);
            }
        }
    }
}
