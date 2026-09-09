# ANF-147 — three-site real balancing preserves the bow gap under exact logarithmic twist

**Status:** `EXACT-DERIVED + REAL-COEFFICIENT-MATCHED-CONTROL + EXACT-TWIST + NEGATIVE/OBSTRUCTION + SOURCE-SPECIFIC-GATE`. `ANF-146` shows that support, coefficient magnitudes, and diagonal mass cannot recover the missing factor `K` in the bow moving-window problem, but its extremal plane-wave controls leave a natural admissibility objection: after the logarithmic carrier is fixed, the arithmetic residual coefficients are real rather than arbitrary complex phases. That objection does not restore coefficient-general coercivity. For **every** prescribed unit-modulus carrier `(z_n)`—in particular the exact Archimedean carrier `z_n=n^{-iU}` at any distinguished twist—one can choose a positive-density real coefficient vector whose length-`K` moving sums are only boundary terms, with `V=O(N)` while its exact moving diagonal is `D asymp NK`. With the same support and the same pointwise coefficient magnitudes, another real sign assignment has `V>=D`. After a harmless `sqrt(log X)` scaling, the two controls have the bow diagonal scale `(1+o(1))XK log X`, obey the crude residual-size bound, and yet one has `o(XK log X)` variance while the other has diagonal-scale variance. Thus **reality of the source coefficients, the exact logarithmic twist, support density, pointwise magnitudes, and the correct diagonal order still do not determine bow coherence**. A successful bow theorem must use a genuinely arithmetic relation among the residual signs/magnitudes and the distinguished twist, or preserve cancellation between arithmetic decomposition pieces.

## 1. Three sites are enough for exact real cancellation against any complex carrier

Fix integers

\[
N\ge 1,
\qquad
1\le K\le N,
\tag{1}
\]

and consider the moving-window operator from `ANF-146`,

\[
(A_{N,K}b)_j
:=
\sum_{r=1}^{K}b_{j+r},
\qquad
0\le j<N,
\tag{2}
\]

on sequences indexed by `1<=n<=N+K-1`. Let

\[
z_n\in\mathbb C,
\qquad |z_n|=1,
\tag{3}
\]

be completely arbitrary and prescribed in advance. We seek **real** coefficients `a_n` and put

\[
b_n:=a_n z_n.
\tag{4}
\]

Take any three consecutive indices `q,q+1,q+2`. Identifying `C` with `R^2`, the three vectors

\[
z_q,\ z_{q+1},\ z_{q+2}\in\mathbb R^2
\tag{5}
\]

are real-linearly dependent. Hence there is a nonzero

\[
c=(c_0,c_1,c_2)\in\mathbb R^3
\tag{6}
\]

such that

\[
\sum_{r=0}^{2}c_r z_{q+r}=0.
\tag{7}
\]

Normalize it by

\[
\sum_{r=0}^{2}c_r^2=1.
\tag{8}
\]

Then

\[
|c_r|\le1,
\qquad
\sum_{r=0}^{2}|c_r|\le\sqrt3.
\tag{9}
\]

Every nonzero relation (7) uses at least two sites, because one nonzero real multiple of a unit complex number cannot vanish. Thus each normalized triple carries at least two nonzero coefficients.

This three-site construction is also the minimal universal local mechanism. For two prescribed phases `z_1,z_2`, a nontrivial real relation

\[
c_1z_1+c_2z_2=0
\tag{10}
\]

exists only when `z_1/z_2` is real, i.e. when the two carrier phases are collinear. Three sites guarantee a real kernel for **every** carrier because the target space has real dimension two.

## 2. Tiling an interior interval makes every moving sum a boundary term

The multiplicity with which coefficient `b_n` appears in the `N` moving windows is

\[
w_n
:=
\#\{0\le j<N:j+1\le n\le j+K\}.
\tag{11}
\]

For the exact interior range

\[
K\le n\le N,
\tag{12}
\]

one has

\[
\boxed{w_n=K.}
\tag{13}
\]

Set

\[
B:=\left\lfloor\frac{N-K+1}{3}\right\rfloor
\tag{14}
\]

and choose the contiguous interior interval

\[
I:=\{K,K+1,\ldots,K+3B-1\}\subseteq\{K,\ldots,N\}.
\tag{15}
\]

Partition `I` into its `B` consecutive triples

\[
T_q:=\{K+3q,K+3q+1,K+3q+2\},
\qquad 0\le q<B.
\tag{16}
\]

For each triple choose a normalized real relation `c^(q)` as in (7)--(8). Given any scale `lambda>0`, define real coefficients by

\[
a_{K+3q+r}:=\lambda c_r^{(q)},
\qquad 0\le r<3,
\tag{17}
\]

and put `a_n=0` outside `I`.

Every full triple has zero twisted sum:

\[
\sum_{n\in T_q}a_n z_n=0.
\tag{18}
\]

Now intersect any moving window

\[
W_j:=\{j+1,\ldots,j+K\}
\tag{19}
\]

with the contiguous interval `I`. The intersection `W_j cap I` is itself an interval. Relative to the triple partition (16), it consists of some number of complete triples plus at most one partial triple at each endpoint. All complete triples disappear by (18). Each partial triple contributes at most

\[
\lambda\sum_{r=0}^{2}|c_r^{(q)}|
\le\sqrt3\lambda.
\tag{20}
\]

Therefore every moving sum satisfies the deterministic bound

\[
\boxed{
|(A_{N,K}b)_j|
\le 2\sqrt3\lambda.
}
\tag{21}
\]

Consequently

\[
\boxed{
V_{N,K}(b)
:=\|A_{N,K}b\|_2^2
\le 12\lambda^2N.
}
\tag{22}
\]

The small output is not caused by sparse energy. Since every coefficient used in (17) lies in the full-multiplicity range (12), its exact moving diagonal is

\[
\begin{aligned}
D_{N,K}(b)
&:=
\sum_{j=0}^{N-1}
\sum_{r=1}^{K}|b_{j+r}|^2\\
&=
\sum_n w_n|a_n|^2\\
&=
K\lambda^2
\sum_{q=0}^{B-1}\|c^{(q)}\|_2^2.
\end{aligned}
\tag{23}
\]

Thus

\[
\boxed{D_{N,K}(b)=K\lambda^2B.}
\tag{24}
\]

Moreover the support contains at least `2B` indices. In particular, whenever

\[
K=o(N),
\tag{25}
\]

one has

\[
B=\frac N3(1+o(1)),
\qquad
D_{N,K}(b)=\frac13(1+o(1))\lambda^2NK,
\tag{26}
\]

while

\[
\boxed{
\frac{V_{N,K}(b)}{D_{N,K}(b)}
\le
\frac{36+o(1)}{K}.
}
\tag{27}
\]

Hence for every prescribed carrier and every `K->infinity` with `K=o(N)`, a positive-density real coefficient vector can have moving variance smaller than its diagonal by a full factor of order `K`.

## 3. The same pointwise magnitudes also admit diagonal-scale energy

The previous vector might conceivably be dismissed as a special choice of coefficient magnitudes. That does not rescue magnitude-based information.

Keep the exact numbers

\[
u_n:=|a_n|
\tag{28}
\]

from (17). For independent Rademacher signs

\[
\varepsilon_n\in\{-1,+1\},
\tag{29}
\]

on the support, define another real coefficient vector

\[
a_n^{(\varepsilon)}:=\varepsilon_nu_n,
\qquad
b_n^{(\varepsilon)}:=a_n^{(\varepsilon)}z_n.
\tag{30}
\]

For each fixed window, independence kills every cross term:

\[
\mathbb E_{\varepsilon}
\left|
\sum_{n\in W_j}\varepsilon_nu_nz_n
\right|^2
=
\sum_{n\in W_j}u_n^2.
\tag{31}
\]

Summing over `j` gives the exact identity

\[
\boxed{
\mathbb E_{\varepsilon}
V_{N,K}(b^{(\varepsilon)})
=D_{N,K}(b).
}
\tag{32}
\]

Therefore at least one deterministic sign assignment satisfies

\[
\boxed{
V_{N,K}(b^{(\varepsilon)})
\ge D_{N,K}(b).
}
\tag{33}
\]

The low-energy vector (17) and this high-energy vector have exactly the same:

- prescribed carrier `(z_n)`;
- real coefficient class;
- support;
- pointwise magnitudes `|a_n|`;
- exact moving diagonal `D_{N,K}`;
- pointwise coefficient bound `|a_n|<=lambda`.

Yet by (27) and (33) their moving-window energies differ by a factor at least of order `K`. Thus even after the complex phase profile is fixed externally, **real signs retain enough local two-dimensional freedom to realize the missing bow coherence scale**.

## 4. Exact specialization to the bow logarithmic carrier

Take integer `X` and reindex the bow coefficients on

\[
X<n\le2X+K
\tag{34}
\]

by `m=n-X`. Then the exact Archimedean carrier at any real twist `U` is

\[
z_m:=(X+m)^{-iU},
\qquad |z_m|=1.
\tag{35}
\]

No Taylor approximation, local linearization, or freedom to replace this carrier by a plane wave is being used. Apply Sections 1--3 directly to (35) with

\[
N=X,
\qquad
K=X^{1-2\epsilon+o(1)},
\qquad
0<\epsilon<\frac14.
\tag{36}
\]

Then `K->infinity` and `K=o(X)`. Choose

\[
\lambda^2:=3\log X.
\tag{37}
\]

The low-energy real control obeys

\[
|a_n|\le\sqrt{3\log X}\ll\log X,
\tag{38}
\]

so it lies well inside the crude pointwise size available for the actual residual `Lambda-Lambda^sharp`. Its exact diagonal satisfies

\[
\boxed{
D_{X,K}
=3K\log X
\left\lfloor\frac{X-K+1}{3}\right\rfloor
=(1+o(1))XK\log X.
}
\tag{39}
\]

This is precisely the bow diagonal order isolated in `ANF-102` and `ANF-145`. Nevertheless (22) gives

\[
\boxed{
V_{X,K}^{\rm low}(U)
\le36X\log X
=o(XK\log X).
}
\tag{40}
\]

The matched real sign assignment from Section 3 has the same support and coefficient magnitudes but satisfies

\[
\boxed{
V_{X,K}^{\rm high}(U)
\ge
(1+o(1))XK\log X.
}
\tag{41}
\]

Both statements hold for **every fixed real `U`**, including `U asymp X^2`, because the construction only uses the exact unit phases (35). Thus the objection to `ANF-146` based on the arithmetic residual being real-valued is decisive only if one also uses its **specific arithmetic sign/magnitude law**. Reality plus the exact logarithmic carrier is still too weak.

There is an important quantifier boundary. The low-energy coefficient vector is allowed to depend on the prescribed carrier and therefore on the selected `U`. It does not contradict `ANF-144`, where one fixed coefficient vector is averaged over a twist interval and every super-`X` interval returns to diagonal scale. The present theorem is a pointwise-in-`U` matched obstruction aimed exactly at the remaining distinguished-twist problem. A theorem that couples the same arithmetic coefficients across a nontrivial family of twists may use information absent here.

## 5. Prior-art boundary and source-specific consequence

The local mechanism is elementary finite-dimensional vector balancing. Classical Steinitz-type results study how bounded zero-sum vectors can be reordered so that partial sums remain bounded, and the planar/complex case has a long literature. That is neighboring prior art, but no Steinitz theorem is used here: the order is fixed, each triple is balanced independently by the two-dimensional real kernel (7), and the moving-window bound follows because an interval can cut at most two triple boundaries. Likewise (32) is the elementary random-sign orthogonality identity. The line-specific result is the exact matched-control consequence for the **fixed logarithmic bow carrier and the bow diagonal normalization**, not a novelty claim about vector balancing itself.

The adversarial boundary is correspondingly strict. These synthetic coefficients are not `Lambda-Lambda^sharp`; their blockwise relations are chosen after the carrier is known, and they encode no prime support, sieve structure, multiplicative factorization, or cross-scale arithmetic consistency. They do not show that the actual distinguished bow residual has small variance. They show that none of the following facts, separately or jointly, can force diagonal-scale variance at one selected twist:

- real-valued coefficients;
- the exact carrier `n^{-iU}` rather than a free plane wave;
- positive-density support;
- a crude `O(log X)` pointwise coefficient bound;
- the correct `XK log X` diagonal order;
- complete knowledge of the coefficient magnitudes.

Accordingly the remaining gate is narrower than the one stated after `ANF-146`. A successful source theorem must exploit information that prevents these local real triple balances for the **actual** residual: for example a quantitative arithmetic correlation between neighboring residual signs and the carrier, a bilinear/multiplicative constraint on the allowed sign patterns, or cancellation preserved between decomposition pieces before absolute values are taken. Merely restoring the facts that the residual is real and that its phase comes from the exact logarithmic twist does not supply the missing `1/K`.