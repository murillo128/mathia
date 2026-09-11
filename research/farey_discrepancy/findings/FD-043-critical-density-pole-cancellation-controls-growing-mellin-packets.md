# FD-043 — critical density-pole cancellation controls growing Mellin packets

**Status:** `EXACT-DERIVED + GROWING-CRITICAL-MELLIN-PACKETS + DENSITY-POLE-CANCELLATION + QUANTITATIVE-OCCUPATION + PHYSICAL-APPROXIMATION-OBSTRUCTION`.

`FD-042` proves universal nonsquarefree Jordan occupation for every fixed finite critical Mellin packet, but leaves growing packet dimension and collapsing frequency separation as possible escape mechanisms. The fixed-packet proof scalarizes the full and nonsquarefree Gram matrices separately, so its constants are not organized for a moving frequency set.

There is a stronger comparison that survives packet growth. Subtract the universal density ratio **before** estimating the Gram matrices. The linear-density terms then cancel exactly, leaving a mean-zero arithmetic weight whose critical Mellin transform is uniformly bounded on every bounded frequency-difference window. Consequently, for an arbitrary moving finite packet, the error in nonsquarefree occupation depends on the packet's coefficient conditioning and frequency diameter, but has **no inverse frequency-gap factor**.

More precisely, for every fixed Schur-head cutoff `D` and every fixed `sigma in (1/2,1)`, if

\[
P(r)=\sum_{j=1}^m z_j r^{-i\gamma_j}
\]

has distinct real frequencies and frequency diameter

\[
\Omega:=\max_{j,k}|\gamma_j-\gamma_k|,
\]

then, uniformly in the row horizon `R`,

\[
\boxed{
\left|
\|P\|_{\mathrm{ns},R,D}^2
-\delta_{\mathrm{ns}}\|P\|_{R,D}^2
\right|
\le
C_{D,\sigma}\,m(1+\Omega)\|z\|_2^2.
}
\]

Here

\[
\|P\|_{R,D}^2
:=\sum_{D<r\le R}\frac{w(r)}r|P(r)|^2,
\qquad
\|P\|_{\mathrm{ns},R,D}^2
:=\sum_{\substack{D<r\le R\\\mu(r)=0}}
\frac{w(r)}r|P(r)|^2,
\]

with `w(r)=J_2(r)/r^2` and the same `delta_ns` as in `FD-038` and `FD-042`.

Therefore every packet family satisfying

\[
\frac{m_R(1+\Omega_R)\|z_R\|_2^2}
     {\|P_R\|_{R,D}^2}
\longrightarrow0
\]

has

\[
\boxed{
\frac{\|P_R\|_{\mathrm{ns},R,D}^2}
     {\|P_R\|_{R,D}^2}
\longrightarrow\delta_{\mathrm{ns}}>0.
}
\]

The remaining critical spectral escape is thus not merely "many frequencies" or "close frequencies". It requires a quantitatively **coherent/ill-conditioned packet** whose full critical row energy is small compared with its coefficient mass, or a remainder that is not negligible in the physical row norm.

## 1. The universal density term cancels before Fourier analysis

Retain the constants from `FD-038`:

\[
a:=\frac1{\zeta(3)},
\qquad
b:=a-c_{\mathrm{sf}},
\qquad
\delta_{\mathrm{ns}}:=\frac ba.
\tag{1}
\]

That finding proves

\[
W(x):=\sum_{r\le x}w(r)=ax+O(1)
\tag{2}
\]

and, for every fixed `sigma>1/2`,

\[
W_{\mathrm{ns}}(x)
:=\sum_{\substack{r\le x\\\mu(r)=0}}w(r)
=bx+O_\sigma(x^\sigma).
\tag{3}
\]

Define the centered arithmetic weight

\[
c(r):=w(r)
\left(\mathbf 1_{\mu(r)=0}-\delta_{\mathrm{ns}}\right).
\tag{4}
\]

Its summatory function is

\[
C(x):=\sum_{r\le x}c(r)
=W_{\mathrm{ns}}(x)-\delta_{\mathrm{ns}}W(x).
\tag{5}
\]

Because `delta_ns=b/a`, the linear terms cancel exactly:

\[
\boxed{
C(x)=O_\sigma(x^\sigma)
\qquad(\sigma>1/2).
}
\tag{6}
\]

This cancellation is the key new organization. If the full and nonsquarefree Gram matrices are estimated separately, their common density contribution produces the large critical `log R` term and near-colliding frequencies produce large common off-diagonal terms. In the **difference relevant to occupation**, all of that common density structure disappears first.

## 2. The centered critical Mellin kernel has no small-gap singularity

For real `t`, set

\[
K_{R,D}(t)
:=\sum_{D<r\le R}c(r)r^{-1+it}.
\tag{7}
\]

Partial summation with (6) gives, uniformly for `R>D`,

\[
\begin{aligned}
K_{R,D}(t)
={}&C(R)R^{-1+it}-C(D)D^{-1+it}\\
&+(1-it)\int_D^R C(x)x^{-2+it}\,dx
+O_D(1),
\end{aligned}
\tag{8}
\]

where the harmless fixed-endpoint term only records the convention at `D`. Since `sigma<1`,

\[
\int_D^\infty x^{\sigma-2}\,dx<\infty.
\tag{9}
\]

Hence

\[
\boxed{
|K_{R,D}(t)|
\le C_{D,\sigma}(1+|t|)
}
\tag{10}
\]

uniformly in `R` and **including `t=0`**.

The last point matters. Estimating the uncentered density term gives an oscillatory integral of size `1/|t|` when `t` is small. Equation (6) removes that term entirely from the occupation difference, so (10) has no factor involving the inverse minimum frequency separation. Frequency collisions can still make a packet badly conditioned in its full norm, but they do not directly enlarge the centered arithmetic kernel.

## 3. Quantitative growing-packet occupation bound

Let

\[
G_{\mathrm{all}}^{(R)}(j,k)
:=\sum_{D<r\le R}\frac{w(r)}r
r^{i(\gamma_j-\gamma_k)},
\tag{11}
\]

\[
G_{\mathrm{ns}}^{(R)}(j,k)
:=\sum_{\substack{D<r\le R\\\mu(r)=0}}
\frac{w(r)}r
r^{i(\gamma_j-\gamma_k)}.
\tag{12}
\]

By (4) and (7), every entry of

\[
\mathcal D_R
:=G_{\mathrm{ns}}^{(R)}
-\delta_{\mathrm{ns}}G_{\mathrm{all}}^{(R)}
\tag{13}
\]

is `K_(R,D)(gamma_j-gamma_k)`. Therefore (10) and the elementary row-sum bound for the operator norm give

\[
\boxed{
\|\mathcal D_R\|_{\mathrm{op}}
\le C_{D,\sigma}m(1+\Omega).
}
\tag{14}
\]

For the packet

\[
P_z(r)=\sum_{j=1}^m z_jr^{-i\gamma_j},
\tag{15}
\]

one has

\[
\|P_z\|_{R,D}^2
=z^*G_{\mathrm{all}}^{(R)}z,
\qquad
\|P_z\|_{\mathrm{ns},R,D}^2
=z^*G_{\mathrm{ns}}^{(R)}z.
\tag{16}
\]

Combining (13)--(16),

\[
\boxed{
\left|
\|P_z\|_{\mathrm{ns},R,D}^2
-\delta_{\mathrm{ns}}\|P_z\|_{R,D}^2
\right|
\le
C_{D,\sigma}m(1+\Omega)\|z\|_2^2.
}
\tag{17}
\]

No separation hypothesis occurs. In particular, whenever the packet-conditioning parameter

\[
\chi_R(P_z)
:=
\frac{m(1+\Omega)\|z\|_2^2}
     {\|P_z\|_{R,D}^2}
\tag{18}
\]

tends to zero,

\[
\boxed{
\frac{\|P_z\|_{\mathrm{ns},R,D}^2}
     {\|P_z\|_{R,D}^2}
=
\delta_{\mathrm{ns}}+O_{D,\sigma}(\chi_R(P_z)).
}
\tag{19}
\]

`FD-042` is recovered when the packet is fixed: its full norm is `(a log R+O(1))||z||_2^2`, so `chi_R=O(1/log R)`. More generally, any moving family with

\[
\|P_R\|_{R,D}^2
\gg (\log R)\|z_R\|_2^2
\tag{20}
\]

and

\[
m_R(1+\Omega_R)=o(\log R)
\tag{21}
\]

still has universal occupation `delta_ns+o(1)`. Thus genuinely growing packet dimension is allowed. The only extra issue is whether the packet keeps its natural critical `log R` energy instead of losing it through coherent cancellation.

## 4. Exact physical row profile turns this into an approximation obstruction

The statement can be applied to the physical source without approximating the floor geometry. For a horizon `H`, define the exact normalized physical row profile

\[
B_H(r)
:=\sqrt{\frac rH}\,
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right),
\qquad D<r\le H.
\tag{22}
\]

Then the definitions of the Schur-tail energies give the exact identities

\[
\boxed{
\|B_H\|_{H,D}^2=\frac{E_{H,D}}H,
\qquad
\|B_H\|_{\mathrm{ns},H,D}^2=\frac{U_{H,D}}H.
}
\tag{23}
\]

Suppose that along an unbounded sequence of horizons there are Mellin packets `P_H` such that

\[
\frac{\|B_H-P_H\|_{H,D}}
     {\|B_H\|_{H,D}}
\longrightarrow0
\tag{24}
\]

and

\[
\chi_H(P_H)\longrightarrow0.
\tag{25}
\]

Because the nonsquarefree norm is dominated by the full norm, (24) also controls the error and cross terms in the numerator. Equations (19), (23)--(25) therefore imply

\[
\boxed{
\frac{U_{H,D}}{E_{H,D}}
\longrightarrow\delta_{\mathrm{ns}}>0.
}
\tag{26}
\]

This is a direct obstruction to the vanishing-occupation scenario of the accepted joint-row clue. A physical sequence with `U_(H,D)/E_(H,D)->0` cannot admit a simultaneously norm-accurate and well-conditioned critical Mellin-packet approximation in the sense of (24)--(25).

The criterion separates two genuinely different ways an infinite-spectrum source could escape. Either every packet satisfying the centered-kernel complexity bound leaves a macroscopic remainder in the exact physical row norm, or accurate packets become so coherent that their coefficient mass is large compared with their actual critical row energy. Merely increasing packet dimension or letting frequencies approach one another is not, by itself, enough.

## 5. Stress tests and boundary cases

The absence of an inverse frequency gap in (17) does **not** say that frequency collisions are harmless for all purposes. If two frequencies nearly coincide with nearly opposite coefficients, the packet can have very small full norm while `||z||_2` stays large; then `chi_R` becomes large and (19) gives no useful relative conclusion. The theorem deliberately records this as packet conditioning rather than hiding it inside a minimum-gap constant.

Likewise, (17) does not control a packet whose dimension and frequency diameter make `m(1+Omega)` comparable with its full critical energy. It also does not prove that the physical source has an approximation satisfying (24). The nontrivial zeros of `zeta` may produce infinitely many comparable frequencies, a remainder of critical size, or coefficient coherence outside every subcritical packet approximation.

The result is invariant under a common translation of all Mellin frequencies, because only differences occur in the Gram matrices and `Omega` is a diameter. This is a useful check against an artificial dependence on absolute spectral height. For one frequency, (17) reduces to a bounded centered diagonal error and reproduces the `O(1/log R)` occupation convergence of the simplest case of `FD-042`.

A direct finite falsification test is available: for any chosen `R,D,Gamma,z`, evaluate the two weighted row norms and the centered quadratic form in (17). A violation of a uniform `C_(D,sigma)m(1+Omega)||z||_2^2` bound as `R` grows would contradict the partial-summation derivation from the summatory laws (2)--(3).

## 6. Prior-art boundary and consequence for the research line

Nonharmonic Fourier frames, separated exponential systems, Hilbert-type inequalities, Abel summation, and Gram-matrix estimates are classical. A targeted prior-art audit found the expected general frame/Dirichlet-polynomial literature; no novelty is claimed for those tools or for a generic statement that well-conditioned exponential packets are stable under a lower-order perturbation. No external theorem is load-bearing here: (17) follows directly from the already-persisted Jordan summatory laws and elementary partial summation.

The Mathia-specific content is the centered Jordan weight (4), the exact cancellation of its density pole, the quantitative occupation comparison (17), and the exact physical-row reduction (22)--(26). Together they sharpen the frontier left by `FD-042`: a critical spectral escape must exhibit **macroscopic nonpacket remainder or quantitative coefficient coherence/ill-conditioning**, not simply a growing or non-separated list of critical frequencies.

This still does not prove a fixed positive `U_(H,D)/E_(H,D)` for the actual Mertens-derived source, so the accepted joint-occupation clue remains open. The next source-specific target is to use the exact increment law

\[
\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n
\]

or the Dirichlet series `zeta(s+1)/zeta(s)` to rule out one of the two remaining alternatives in (24)--(25): persistent critical-norm approximation failure or increasingly ill-conditioned Mellin representations.