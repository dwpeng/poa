# POA

```python
from poa import Graph, read_file

match = 2
mismatch = -1
gap = -2
g = Graph()

sequence, alignment = read_file('test.fa', 'fasta')
g.init_graph_by_seq(sequence[0])
for seq in sequence[1:]:
    g.add_seq_to_align(alignment(
        g, 
        seq, 
        match=match, 
        mismatch=mismatch, 
        gap=gap
    ))

g.to_msa(open('msa.txt', 'w'))
```
