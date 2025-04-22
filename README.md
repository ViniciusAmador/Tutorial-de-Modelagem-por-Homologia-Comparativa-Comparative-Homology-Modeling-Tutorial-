
<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/Tutorial-Comparative%20Homology%20Modeling-green" alt="Tutorial">
  <img src="https://img.shields.io/badge/Tool-Modeller-blueviolet" alt="Modeller">
  <img src="https://img.shields.io/badge/status-Active-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Written%20in-Markdown-orange" alt="Markdown">
</p>

## 🧬 Tutorial de Modelagem por Homologia Comparativa | Comparative Homology Modeling Tutorial | 比较同源建模教程

### 🌐 Sobre este tutorial | About this tutorial | 关于本教程
Este guia ensina como realizar **modelagem por homologia comparativa** de proteínas usando **Modeller**, a partir de uma estrutura molde obtida via SwissModel e uma sequência alvo.

This guide teaches you how to perform **comparative homology protein modeling** using **Modeller**, based on a template structure obtained via SwissModel and a target sequence.

本教程将指导你如何使用 **Modeller** 软件，通过 SwissModel 获得模板结构，并结合目标序列进行蛋白质的 **比较同源建模**。

---

### 📁 Pré-requisitos | Requirements | 前提条件
- Python instalado com Modeller (ex: `mod9.23`, `mod9.25`)
- Diretório contendo:
  - Estrutura PDB do molde (template)
  - Arquivo `.ali` da sequência alvo

---

🗂️ Estrutura recomendada do diretório | Recommended folder structure | 推荐的目录结构

```bash
homology_modeling_project/
├── align2d.py                 # Script de alinhamento entre molde e alvo
├── model-single.py            # Script de modelagem por homologia
├── template.ali               # Arquivo .ali contendo sequência do molde (template)
├── alvo.ali                   # Arquivo .ali com a sequência da proteína alvo
├── nome_do_template.pdb       # Estrutura tridimensional do molde (PDB)
├── alvo-template.ali          # Gerado após alinhamento
├── alvo-template.pap          # Alinhamento em formato PAP (opcional)
├── model-single.log           # Log do processo de modelagem
├── out                        # Arquivo com scores extraídos
└── modelos/                   # (Opcional) Pasta onde os modelos podem ser salvos
```
---

### ✍️ Etapa 1: Criação do Arquivo `.ali` | Step 1: Create the `.ali` File | 第一步：创建 `.ali` 文件

Este arquivo deve conter a sequência da proteína alvo formatada para o Modeller. Exemplo:

```bash
>P1;alvo
sequence:alvo::::::::
SEQUENCIADASEQUENCIASEQUENCIASEQUENCIA*
```

---

### 🔗 Etapa 2: Alinhamento | Step 2: Alignment | 第二步：比对结构

Use o comando no terminal:
```bash
mod9.23 align2d.py
```

#### align2d.py:
```python
from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='nome do template', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='nome do template', atom_files='nome do template.pdb')
aln.append(file='template.ali', align_codes='template')
aln.align2d()
aln.write(file='alvo-template.ali', alignment_format='PIR')
aln.write(file='alvo-template.pap', alignment_format='PAP')
```

---

### 🧪 Etapa 3: Modelagem por Homologia Comparativa | Step 3: Comparative Homology Modeling | 第三步：进行比较同源建模

Use o seguinte comando no terminal:
```bash
mod9.25 model-single.py
```

#### model-single.py:
```python
from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env, alnfile='template.ali',
              knowns='template', sequence='alvo',
              assess_methods=(assess.DOPE, assess.GA341))
a.starting_model = 1
a.ending_model = 5   # Gera 5 modelos

a.make()
```

---

### 📊 Etapa 4: Avaliação de Modelos | Step 4: Model Evaluation | 第四步：模型评估

Use os comandos abaixo para extrair e ordenar as métricas do DOPE score:

```bash
tail -103 model-single.log > out
sort -k 3 -r out
```

> 🧠 Nota: usamos `103` porque há 3 linhas de cabeçalho extras.

---

### 📚 Referências | References | 参考资料
- Modeller: https://salilab.org/modeller/
- SwissModel: https://swissmodel.expasy.org
- DOPE score explanation: https://salilab.org/modeller/manual/node199.html
- ŠALI, A.; BLUNDELL, T. L. Comparative protein modelling by satisfaction of spatial restraints. *Journal of Molecular Biology*, 234(3), 779–815, 1993. DOI: https://doi.org/10.1006/jmbi.1993.1626

---

**Precisa de ajuda para interpretar os modelos gerados?**
📩 Entre em contato!

Need help interpreting your models? Contact me!

你需要帮助来解释这些模型吗？欢迎联系我！
