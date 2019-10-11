#!/usr/bin/env python3

sentence = input()

sentence = sentence.replace('apa', 'a')
sentence = sentence.replace('epe', 'e')
sentence = sentence.replace('ipi', 'i')
sentence = sentence.replace('opo', 'o')
sentence = sentence.replace('upu', 'u')
        
print(*sentence, sep='')