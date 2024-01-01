n="Comrade AP's Audio Sources 8.wav"

# Import the AudioSegment class for processing audio and the
# split_on_silence function for separating out silent chunks.
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

# Load your audio.
song = AudioSegment.from_wav(n)

# Split track where the silence is 2 seconds or more and get chunks using
# the imported function.
chunks = split_on_silence (
    # Use the loaded audio.
    song,
    # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
    min_silence_len = 150,
    # Consider a chunk silent if it's quieter than -16 dBFS.
    # (You may want to adjust this parameter.)
    silence_thresh = -28
)

if not os.path.exists(pa:='.'.join(n.split('.')[:-1])):os.mkdir(pa)
# Process each chunk with your parameters
for i, chunk in enumerate(chunks):
    # Export the audio chunk with new bitrate.
    print("Exporting chunk%s.wav."%(str(i).rjust(6).replace(' ','0')))
    chunk.export(
        "./%s/chunk%s.wav"%(pa,str(i).rjust(6).replace(' ','0')),
        bitrate = "44100",
        format = "wav"
    )
