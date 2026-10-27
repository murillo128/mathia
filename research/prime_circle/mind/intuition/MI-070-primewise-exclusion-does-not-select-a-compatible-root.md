# MI-070 — Every hole can be separable while the root choices remain incompatible

**Evidence level:** supported by
[PC-472](../../findings/PC-472-primewise-separation-does-not-ensure-compatible-root-selection.md),
with the compatible coding and finite-support realization in
[PC-471](../../findings/PC-471-compatible-root-phases-retain-full-spectrum-but-generically-collapse.md).
This is exact selection geometry within classical residue coding, not a
prime-specific spectral law.

For one nonzero forbidden residue `r_p` at each prime, write

\[
C(r)=\{h\in\mathbb Z:h\not\equiv r_p\pmod p\ \forall p\},\qquad
\mathcal C_0=\{C(r):r_p\ne0\}.
\]

A rooted admissible support `S` contains zero and omits a residue at every
prime. Define

\[
\operatorname{cl}_{\rm pr}S
=\{h:h\bmod p\in S\bmod p\ \forall p\},\qquad
W_h(S)=\{p:h\bmod p\notin S\bmod p\}.
\]

Equality `cl_pr S=S` says each hole has an available exclusion prime.
It does not supply **one simultaneous choice** of residues killing all
holes. This closure tests prime moduli, not all composite moduli.

PC-472 constructs a partial sieve
`T={h:h!=r_q mod q for every q!=3}` retaining `0,2,4`, such that
`S=T intersect 3Z` is infinite and
`S mod q=(Z/qZ) minus {r_q}` for every `q!=3`. The infinite realization
is essential: at each prime `q!=3`, CRT installs witnesses in `3Z` for every
allowed residue. Before inserting them, freeze all unassigned primes other
than three up to the new point count. Every later choice avoids all installed witnesses
and `2,4`; larger unassigned primes cannot yet be saturated by the finite
set. Additional survivors remain in `S`; it is not just the installed
witness list.

Then `cl_pr S=S`, but `W_2(S)=W_4(S)={3}`. Killing `2` requires `r_3=2`,
whereas killing `4` requires `r_3=1`. The only compatible supersets are

\[
C_1=T\setminus(1+3\mathbb Z),\qquad
C_2=T\setminus(2+3\mathbb Z),\qquad C_1\cap C_2=S\notin\mathcal C_0.
\]

Thus the exact compatible image is not even closed under binary
intersection of this kind. An individual exclusion witness is weaker
than jointly consistent root selection.

There is also a precise sufficient repair: if `W_h(S)` is infinite for
every hole, the phases killing that hole form an open dense subset of
`product_p((Z/pZ) minus (S mod p))`. Every finite cylinder leaves a fresh
available prime. Baire's theorem then kills all countably many holes
simultaneously. This is sufficient, not necessary.

For the zero-extended Cauchy operator
`(L_S)_(hk)=1_(h,k in S) i/(pi(h-k))` off the diagonal, with zero diagonal,
every compatible completion preserving `S` retains either `2` or `4`.
Hence `||(L_C-L_S)e_0||>=1/(4pi)`. This is **not** separation from the
closure of all compatible operators: the finite truncations
`F_R=S intersect [-R,R]` are compatible and `L_(F_R)->L_S` strongly,
by the bounded-operator and column-tail bounds of
[PC-465](../../findings/PC-465-moving-center-cotangent-limits-fill-the-admissible-hull.md).
Their phases may change as `R` grows. No spectral-set or spectral-type
separation follows from this exact-support obstruction.
