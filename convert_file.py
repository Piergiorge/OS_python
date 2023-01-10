import os
import io

# Open the input file in binary mode
with open('input.txt', 'rb') as f:
    # Read the contents of the file
    contents = f.read()

# Replace the Windows line endings (b'\r\n') with Unix line endings (b'\n')
contents = contents.replace(b'\r\n', b'\n')

# Open the output file in binary mode
with open('output.txt', 'wb') as f:
    # Write the modified contents to the output file
    f.write(contents)
