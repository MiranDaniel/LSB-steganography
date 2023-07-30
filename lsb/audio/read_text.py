import wave
import struct


def read(audio_path):
    with wave.open(audio_path, "rb") as audio_file:
        num_frames = audio_file.getnframes()
        sample_width = audio_file.getsampwidth()
        frames = audio_file.readframes(num_frames)

        binary_message = ""
        message_length = None
        message_index = 0

        # Extract the message from the LSB of each audio sample
        for i in range(0, len(frames), sample_width):
            current_sample = frames[i : i + sample_width]
            sample_value = struct.unpack("<h", current_sample)[0]
            lsb = sample_value & 1
            binary_message += str(lsb)

            # if message_length is not None and message_index == message_length:
            #    break

            # If the message length is not yet determined, check if the length is fully extracted
            if message_length is None and len(binary_message) % 8 == 0:
                message_length = int(binary_message, 2)

            # If the message length is determined, check if the entire message is extracted
            if message_length is not None and len(binary_message) >= message_length + 8:
                message_index += 8

        extracted_message = ""
        for i in range(0, len(binary_message) - 8, 8):
            byte = binary_message[i : i + 8]
            char = chr(int(byte, 2))
            extracted_message += char

        return extracted_message
