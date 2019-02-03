#!/usr/bin/env python3

import mkchain
import shelve

def train_text(input_file, model_file = 'data'):
    model = mkchain.train('Life is Love.'.lower().split())

    with open(input_file+'.txt') as dataset:
        for line in dataset:
            text = line.lower().split()
            model = mkchain.train(text, model)

    with shelve.open(model_file) as data:
        data['Model'] = model


def generate_text(model_file = 'data', output_file ='rick_output', amount = 1):
    with shelve.open(model_file) as data:
        model = data['Model'] 


    with open(output_file+'.txt', '+w') as file:
        for i in range(amount):
            while True:
                txt = mkchain.generate(model, length=30)
                if len(txt) > 20:
                    break
            
            file.write(' '.join(txt) + '\n\n')
def generate_text2(model_file = 'data', output_file ='morty_output', amount = 1):
    with shelve.open(model_file) as data:
        model = data['Model'] 


    with open(output_file+'.txt', '+w') as file:
        for i in range(amount):
            while True:
                txt = mkchain.generate(model, length=30)
                if len(txt) > 20:
                    break
            
            file.write(' '.join(txt) + '\n\n')


train_text('rick')
generate_text()
train_text('morty')
generate_text2()
