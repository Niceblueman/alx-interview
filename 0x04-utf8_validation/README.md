##  0x04. UTF-8 Validation 

**Read or watch**:

- UTF-8
- Characters, Symbols, and the Unicode Miracle
> General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable


**Method:**`FSS-UTF (1992) / UTF-8 (1993)`
- from U+0000 to U+007F is size 0 with check of >> 7(byte size - 1) to find MSB (byte one) 0b0
- from U+0080 to U+07FF is size 1 with check of >> 5 to find MSB 0b110
- from U+0800 to U+FFFF is size 2 with check of >> 4 to find MSB 0b1110
- from U+10000 to U+1FFFFF is size 3 with check of >> 3 to find MSB 0b11110
- from U+200000 to U+3FFFFFF is size 4 with check of >> 2 to find MSB 0b111110
- from U+4000000 to U+7FFFFFFF is size 5 with check of >> 1 to find MSB 0b1111110
- in case of U+0080 	U+207F 	10xxxxxx `FSS-UTF proposal (1992) Number` size --1 and check MSB with >> 6 shift to find 0b110




