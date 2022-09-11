from pydub import AudioSegment

m4a_file = r"Grabación.m4a"
MP3_filename = r"Grabación.mp3"
track = AudioSegment.from_file(m4a_file,  format= 'm4a')
file_handle = track.export(MP3_filename, format='mp3') 