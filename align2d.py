from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='nome_do_template', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='nome_do_template', atom_files='nome_do_template.pdb')
aln.append(file='template.ali', align_codes='template')
aln.align2d()
aln.write(file='alvo-template.ali', alignment_format='PIR')
aln.write(file='alvo-template.pap', alignment_format='PAP')