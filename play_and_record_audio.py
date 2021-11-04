import wave
import pyaudio

audio = pyaudio.PyAudio()

FORMAT = pyaudio.paInt16 # We use 16bit format per sample
CHANNELS = 2
RATE = 8000
CHUNK = 1024 # 1024bytes of data red from a buffer
RECORD_SECONDS = 0.1

wf = wave.open("file_example_WAV_1MG.wav", 'rb')

stream_in = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True)#,
                    #frames_per_buffer=CHUNK)
stream_in.start_stream()

stream_out = audio.open(format=FORMAT,
                       channels=2,
                       rate=RATE,
                       output=True)


def get_data():
    return wf.readframes(CHUNK)
    return stream_in.read(CHUNK)

data=get_data()
while len(data) > 0:
    stream_out.write(data)
    data = get_data()