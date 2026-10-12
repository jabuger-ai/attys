#ifndef ATTYS_ECG_AMBIENTAUDIO_H
#define ATTYS_ECG_AMBIENTAUDIO_H

#include <oboe/Oboe.h>
#include <math.h>
#include <android/asset_manager.h>
#include <vector>
#include <string>
#include <memory>
#include "util.h"

using namespace oboe;

static constexpr int samplingRate = 48000;
const std::string nameBackgroundSound = "ocean-waves.pcm";
static constexpr int numOfWaveSounds = 5;
static constexpr int buffersize = 4;
const std::string namesOfWaves[numOfWaveSounds] = {"wave1.pcm",
                                                   "wave2.pcm",
                                                   "wave3.pcm",
                                                   "wave4.pcm",
                                                   "wave5.pcm"};

class AmbientAudio {
public:
    void init(AAssetManager *aAssetManager);
    void start();
    void stop();
    void hasHR(float hr);

private:

    struct __attribute__ ((packed)) FrameData {
        float left;
        float right;
    };

    class MyCallback : public oboe::AudioStreamDataCallback {
    public:
        oboe::DataCallbackResult
        onAudioReady(oboe::AudioStream *audioStream, void *audioData, int32_t numFrames) override;
        AmbientAudio* ambientAudio = nullptr;
    };

    class AudioSource {
    public:
        void loadWAV(AAssetManager *aAssetManager, const std::string &name);
        void fillBuffer(FrameData* buffer, int numFrames, float gain = 1.0f);
        void play(bool doLoopPlaying = true);
        void stop() { isPlaying = false; }
    private:
        std::vector<FrameData> wave;
        size_t offset = 0;
        size_t offset2 = 0;
        bool isPlaying = false;
        bool loopPlaying = false;
    };

    AudioSource waveSounds[numOfWaveSounds];
    AudioSource backgroundSound;

    MyCallback myCallback;
    std::shared_ptr<oboe::AudioStream> mStream;
    std::vector<float> hrBuffer;
};

#endif // ATTYS_ECG_AMBIENTAUDIO_H
