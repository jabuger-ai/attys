#include <jni.h>
#include <android/asset_manager_jni.h>
#include "AmbientAudio.h"

static AmbientAudio gAmbientAudio;

extern "C" JNIEXPORT void JNICALL
Java_tech_glasgowneuro_attysecg_AmbientAudioEngine_nativeInit(
        JNIEnv *env,
        jobject /* this */,
        jobject assetManager) {
    AAssetManager *mgr = AAssetManager_fromJava(env, assetManager);
    if (mgr) {
        gAmbientAudio.init(mgr);
    }
}

extern "C" JNIEXPORT void JNICALL
Java_tech_glasgowneuro_attysecg_AmbientAudioEngine_nativeStart(
        JNIEnv *env,
        jobject /* this */) {
    gAmbientAudio.start();
}

extern "C" JNIEXPORT void JNICALL
Java_tech_glasgowneuro_attysecg_AmbientAudioEngine_nativeStop(
        JNIEnv *env,
        jobject /* this */) {
    gAmbientAudio.stop();
}

extern "C" JNIEXPORT void JNICALL
Java_tech_glasgowneuro_attysecg_AmbientAudioEngine_nativeSendHR(
        JNIEnv *env,
        jobject /* this */,
        jfloat hr) {
    gAmbientAudio.hasHR(hr);
}
