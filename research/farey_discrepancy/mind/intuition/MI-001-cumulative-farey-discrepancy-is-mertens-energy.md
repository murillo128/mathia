# MI-001 — Farey frontier anchor packets compress to subpower predecessor entropy, but fixed-strength composition remains open

**Evidence level:** supported by the exact physical occupation reductions through FD-084, the matched geometric control FD-085, the divisor-supported transport inequality FD-086, the exact dilation/terminal-sector bounds FD-087, the repeated-prime deflation construction FD-088, and the canonical predecessor compression FD-089. No theorem yet gives recursively iterable fixed-strength multiplicative transport.

FD-071--FD-084 show that every sufficiently late fixed-power future window contains a constant-strength occupied block of length `L_H=H^(Theta-delta)`. FD-085 proves that abundance and even linear additive blocks do not by themselves imply a bounded-ratio integer chain, while FD-086 shows that the complete physical Jordan vectors are projectively coherent throughout each such block.

FD-087 tests exact inter-block transport and separates two issues. Integer dilation is uniformly well conditioned, so exact copies themselves are not information-destroying. But every exact copy forced from an anchor `a<=L_H` lies in the terminal quotient sector, and the normalized energy of the entire sector tends to zero. Small common anchors therefore cannot transport the bulk frontier packet.

FD-088 escapes that capacity obstruction: a fixed positive share of the nonsquarefree frontier energy can be stitched with vanishing Hilbert distortion and represented by exact unit-weight lower anchors `a_r >> sqrt(H L_H) >> L_H`. The apparent cost is row dependence.

FD-089 shows that this row dependence has only subpower entropy at the exponent level. Large repeated-prime labels carry negligible frontier energy, and all rows assigned to one small repeated prime can be rounded to the canonical predecessor `A_p=ceil(H/p)`. Along a diagonal frontier sequence the whole positive-energy packet is therefore carried by only `H^{o(1)}` predecessor states at scale `H^{1-o(1)}`. Pigeonholing yields one predecessor with

`E_(A_H,1) >= H^{-o(1)} E_(H,1)`

and the same frontier exponent `2 Theta`.

The obstruction has moved again. The compressed family is not yet a finite-strength recurrence: the selected predecessor may have no positive nonsquarefree occupation, the guaranteed share can vanish subpolynomially, and the occupied-block theorem works in fixed-power future windows rather than the much narrower subpower interval needed to iterate the predecessor selection. The next theorem must upgrade overlap/occupation, compose the `H^{o(1)}` family across blocks, or show that even this zero-entropy family can remain multiplicatively incompatible.

**Boundary.** The clean positive-mass statement is at `D=1`; fixed larger heads retain only a finite exceptional band. FD-089 is conditional on the false-RH frontier setup and does not itself produce an inter-block multiplicative chain, contradiction, or RH proof. Subpower predecessor count is an exponent-level compression, not a claim that one predecessor carries a fixed positive fraction.