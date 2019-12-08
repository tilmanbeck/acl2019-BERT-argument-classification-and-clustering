import json


train = ['']
dev = ['death_penalty']
test = ['gun_control', 'school_uniforms']

file_names = {
    'train': ['aspect_detection_marijuana_legalization_ibcc.jsonl', 'aspect_detection_minimum_wage_ibcc.jsonl',
              'aspect_detection_nuclear_energy_ibcc.jsonl', 'aspect_detection_cloning_ibcc.jsonl',
              'aspect_detection_abortion_ibcc.jsonl', 'aspect_detection_death_penalty_ibcc.jsonl'],
    'test': ['aspect_detection_gun_control_ibcc.jsonl', 'aspect_detection_school_uniforms_ibcc.jsonl']
}
complete = []
for split,fnames in file_names.items():
    for fn in fnames:
        with open('./' + fn, 'r') as fp:
            for line in fp:
                dat = json.loads(line)
                dat['split'] = split
                complete.append(dat)

with open('data.tsv', 'w') as fp:
    for d in complete:
        fp.write('\t'.join([d['topic'], d['hash'], d['sentence'], d['stance'], d['split']]) + '\n' )
