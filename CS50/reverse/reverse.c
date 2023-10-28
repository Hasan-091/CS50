#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{

    if (argc != 3)
    {
        printf("Usage: reverse.c input.wav output.wav\n");
        return 1;
    }

    char *infile = argv[1];
    FILE *inptr = fopen(infile, "rb");
    if (inptr == NULL)
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }

    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, inptr);

    if (check_format(header) == 0)
    {
        fclose(inptr);
        printf("Output is not a WAV file.\n");
        return 1;
    }

    if (header.audioFormat != 1)
    {
        fclose(inptr);
        printf("Audio format is not PCM.\n");
        return 1;
    }

    char *outfile = argv[2];
    FILE *outptr = fopen(outfile, "wb");
    if (outptr == NULL)
    {
        printf("Could not open %s.\n", outfile);
        return 1;
    }

    fwrite(&header, sizeof(WAVHEADER), 1, outptr);

    int size = get_block_size(header);

    if (fseek(inptr, size, SEEK_END))
    {
        return 1;
    }

    BYTE buffer[size];
    while (ftell(inptr) - size > sizeof(header))
    {

        if (fseek(inptr, -2 * size, SEEK_CUR))
        {
            return 1;
        }
        fread(buffer, size, 1, inptr);
        fwrite(buffer, size, 1, outptr);
    }

    fclose(inptr);

    fclose(outptr);
}

int check_format(WAVHEADER header)
{
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    int size = header.numChannels * header.bitsPerSample / 8;
    return size;
}