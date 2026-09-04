# WI-151 — phase-masked combs force a pointwise bounded-depth spectral floor

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-149 showed that full bounded-depth Lamzouri-form scalar universality forces Gaussian-smoothed positivity, while WI-150 replaced the Gaussian microscope by a fixed-period binomial comb and obtained an exact lattice-alias inequality for compactly supported profiles. WI-150 deliberately left one escape open: a negative inner spectral value `phi(a)` could be repaired by positive mass at harmonics `2a,3a,...`. The phase-masked comb below closes that escape under the same **full universal scalar finite-multiset hypothesis**. The conclusion is pointwise, requires neither compact spectral support nor a derivative bound on `phi`, and quantifies the only remaining central-screening cost.

Let `B>0`, let `phi : R -> R` be continuous and real-even, normalized by

\[
\int_{\mathbb R}\phi(t)\,dt=1,
\tag{1}
\]

and assume

\[
\int_{\mathbb R}|\phi(t)|e^{4\pi B|t|}\,dt<\infty.
\tag{2}
\]

Define

\[
H(z)=\int_{\mathbb R}\phi(t)e^{-2\pi i zt}\,dt
\qquad (|\operatorname{Im}z|\le2B).
\tag{3}
\]

Suppose the Lamzouri-form scalar inequality

\[
s(\mathcal Z)\ge 2|\mathcal Z|-\sum_{z,w\in\mathcal Z}H(z-w)
\tag{4}
\]

holds for every nonempty finite conjugation-invariant multiset `Z` contained in `|Im z|<=B`. Then

\[
\boxed{\phi(0)\ge0}
\tag{5}
\]

and, for every `a>0`,

\[
\boxed{
\phi(a)\ge
-2\phi(0)\operatorname{sech}^{2}(2\pi Ba).
}
\tag{6}
\]

In particular,

\[
\boxed{
\phi(a)\ge-8\phi(0)e^{-4\pi Ba}.
}
\tag{7}
\]

Thus the higher-harmonic repair channel left open by WI-150 is not intrinsic to bounded physical depth. It is an artifact of using an unmasked periodic comb. A positive horizontal phase mask can annihilate every lattice alias except `0` and `+-a`, after which bounded-depth universality itself forces the pointwise floor (6).

## 1. Universal integer multiplicities imply copositivity for positive horizontal measures

For a finite conjugation-invariant multiset `Z`, use the notation of WI-149--WI-150,

\[
S_{\mathcal Z}(t)=\sum_{z\in\mathcal Z}e^{-2\pi i tz},
\qquad
Q_H(\mathcal Z)=\sum_{z,w\in\mathcal Z}H(z-w).
\tag{8}
\]

The exponential moment (2) justifies Fubini for points in the strip, and conjugation invariance gives

\[
Q_H(\mathcal Z)
=
\int_{\mathbb R}\phi(t)|S_{\mathcal Z}(t)|^2\,dt.
\tag{9}
\]

Fix `0<b<B`. Take only non-real conjugate pairs `x_j+-ib`, with positive integer horizontal multiplicities `m_j`. Since `s(Z)=0`, (4) gives

\[
Q_H(\mathcal Z)\ge2|\mathcal Z|.
\tag{10}
\]

If every multiplicity is multiplied by an integer `q`, the left side scales as `q^2` while the right side scales as `q`. Dividing by `q^2` and taking `q->infinity` therefore yields

\[
\int_{\mathbb R}
\phi(t)\cosh^2(2\pi bt)
\left|
\sum_j m_j e^{-2\pi i t x_j}
\right|^2dt
\ge0.
\tag{11}
\]

Rational approximation of positive coefficients and then weak approximation of a compactly supported finite positive measure by positive atomic measures extend (11) to every such measure `nu`:

\[
\boxed{
\int_{\mathbb R}
F_b(t)|\widehat\nu(t)|^2dt\ge0,
\qquad
F_b(t):=\phi(t)\cosh^2(2\pi bt).
}
\tag{12}
\]

The limiting step is harmless: `|widehat nu(t)|` is bounded by the total mass, and (2) makes `F_b` integrable. Equation (12) is a copositivity statement for positive horizontal measures. It is strictly weaker than positive definiteness for arbitrary signed coefficients, but it is stronger than testing only the raw equal-weight combs used in WI-150.

## 2. A positive phase mask annihilates the higher lattice aliases

Fix `a>0`. On the horizontal phase interval `[0,1/a]`, define the probability measure

\[
d\mu_a(x)
=
a\bigl(1+\cos(2\pi ax)\bigr)\,dx.
\tag{13}
\]

The density is nonnegative. Its Fourier transform `A_a(t)=widehat mu_a(t)` satisfies, at the lattice `a Z`,

\[
A_a(0)=1,
\qquad
A_a(\pm a)=\frac12,
\qquad
A_a(na)=0\quad(|n|\ge2).
\tag{14}
\]

Moreover, because `mu_a` is supported in `[0,1/a]`,

\[
|A_a'(t)|
\le\frac{2\pi}{a}
\qquad(t\in\mathbb R).
\tag{15}
\]

Now take the normalized binomial probability measure

\[
\beta_m
=2^{-m}\sum_{j=0}^{m}\binom mj\delta_{j/a}.
\tag{16}
\]

Then

\[
|\widehat\beta_m(t)|^2
=
\cos^{2m}\!\left(\frac{\pi t}{a}\right).
\tag{17}
\]

The convolution `nu_m=mu_a*beta_m` is again a positive compactly supported probability measure, so (12) yields

\[
J_m:=
\int_{\mathbb R}
F_b(t)|A_a(t)|^2K_m(t)\,dt
\ge0,
\tag{18}
\]

where

\[
K_m(t)
=
\frac{4^m}{a\binom{2m}{m}}
\cos^{2m}\!\left(\frac{\pi t}{a}\right).
\tag{19}
\]

As in WI-150, `K_m` is `a`-periodic and has mass one on every centered period cell. It is an approximate identity at each lattice point `na`.

The only point that needs checking beyond WI-150 is that the infinitely many cells are harmless even though `phi` is not compactly supported. On a cell `na+[-a/2,a/2)`, with `|n|>=2`, (14)--(15) give

\[
|A_a(na+u)|^2
\le \left(\frac{2\pi}{a}\right)^2u^2.
\tag{20}
\]

The classical Wallis bound gives

\[
\frac{4^m}{\binom{2m}{m}}=O(\sqrt m),
\tag{21}
\]

and the elementary estimate `cos x <= exp(-2x^2/pi^2)` for `|x|<=pi/2` gives

\[
\sup_{|u|\le a/2}u^2K_m(u)=O(m^{-1/2}).
\tag{22}
\]

Therefore the absolute contribution of all cells `|n|>=2` is at most

\[
O(m^{-1/2})\,\|F_b\|_{L^1}
\longrightarrow0.
\tag{23}
\]

On the three surviving cells, the ordinary approximate-identity limit and (14) give

\[
J_m\longrightarrow
F_b(0)+\frac14F_b(a)+\frac14F_b(-a)
=
\phi(0)+\frac12\phi(a)\cosh^2(2\pi ba).
\tag{24}
\]

Since every `J_m>=0`,

\[
\boxed{
\phi(0)+\frac12\phi(a)\cosh^2(2\pi ba)\ge0
}
\qquad(0<b<B).
\tag{25}
\]

## 3. The central value is nonnegative, hence the pointwise floor

To isolate the origin, replace (13) by Haar probability measure on `[0,1/a]`,

\[
d\mu_{a,0}(x)=a\,dx.
\tag{26}
\]

Its Fourier transform equals `1` at `0` and vanishes at every nonzero lattice point `na`. Repeating the same masked-comb argument gives

\[
\boxed{\phi(0)\ge0.}
\tag{27}
\]

Now let `b\uparrow B` in (25). Continuity in `b` gives

\[
\phi(0)+\frac12\phi(a)\cosh^2(2\pi Ba)\ge0,
\tag{28}
\]

which is exactly (6). Finally `sech^2 x<=4e^{-2x}` for `x>=0` yields (7).

This is substantially sharper than the regularity-based moving-family statement of WI-149. If `B_T->infinity`, every `phi_T` satisfies the corresponding full scalar universality, and

\[
\sup_T\phi_T(0)\le M<\infty,
\tag{29}
\]

then for every fixed `a>0`,

\[
\boxed{
\phi_T(a)
\ge
-8M e^{-4\pi B_Ta}.
}
\tag{30}
\]

No uniform `L^infinity`, Lipschitz, compact-support, or derivative hypothesis is needed. A fixed-radius negative dip of fixed amplitude can survive only if the central value grows exponentially in the available depth, the negative feature moves toward the origin on a shrinking scale, or the scalar inequality ceases to be universal over all finite conjugation-invariant configurations.

## 4. Compact support: the best finite alias-annihilating phase mask

There is a useful finite-support sharpening that also places WI-150's outer-half estimate in a classical truncated moment problem. Assume additionally

\[
\operatorname{supp}\phi\subset[-S,S],
\qquad 0<a\le S,
\tag{31}
\]

and put

\[
N:=\left\lfloor\frac Sa\right\rfloor\ge1.
\tag{32}
\]

Seek a positive probability measure on the phase circle whose Fourier moments satisfy

\[
m_0=1,
\qquad
m_{\pm1}=c,
\qquad
m_{\pm k}=0\quad(2\le k\le N).
\tag{33}
\]

The associated `(N+1)x(N+1)` Toeplitz moment matrix is tridiagonal, with diagonal `1` and first off-diagonal `c`. Its eigenvalues are

\[
1+2c\cos\frac{k\pi}{N+2},
\qquad 1\le k\le N+1.
\tag{34}
\]

Hence it is positive semidefinite exactly when

\[
0\le c\le
c_N:=\frac{1}{2\cos(\pi/(N+2))}.
\tag{35}
\]

By the classical Caratheodory--Fejer/Vandermonde decomposition for positive semidefinite Toeplitz matrices, the endpoint `c=c_N` is realized by a finite positive atomic probability measure. Applying the masked comb with this phase measure leaves, inside the support of `phi`, only the aliases `0` and `+-a`. Therefore

\[
\phi(0)+2c_N^2\phi(a)\cosh^2(2\pi Ba)\ge0,
\tag{36}
\]

so

\[
\boxed{
\phi(a)
\ge
-2\cos^2\!\left(\frac{\pi}{N+2}\right)
\phi(0)\operatorname{sech}^2(2\pi Ba).
}
\tag{37}
\]

For `N=1`, the coefficient is `1/2`, exactly recovering WI-150's outer-half floor. As `N->infinity` the coefficient tends to `2`, matching the noncompact mask (13). Thus the constant in (37) is optimal **within positive phase masks required to annihilate every lattice alias `2a,...,Na`**; no global optimality among all possible finite-multiset probes is claimed.

## 5. Consequence for the bounded-depth signed-scalar program

WI-150 identified higher harmonic aliases as the surviving fixed-period screening mechanism for an inner negative dip. Equations (25)--(28) show that this mechanism disappears once one permits a positive phase mask before the same binomial comb. The scalar program therefore has a much stronger rigidity than the raw lattice test suggested:

\[
\boxed{
\text{full bounded-depth scalar universality}
\Longrightarrow
\phi(a)\ge-2\phi(0)\operatorname{sech}^2(2\pi Ba)
\quad\text{for every }a>0.
}
\tag{38}
\]

This does **not** prove `phi>=0` at fixed finite `B`, and it does not produce a new zeta-zero proportion. At finite depth the central value can still screen a negative point. But for a moving family with increasing available depth and controlled `phi_T(0)`, the screening budget decays exponentially at every fixed positive radius. Consequently, optimizing increasingly deep universal scalar kernels cannot maintain a fixed negative Fourier feature away from the origin merely by rearranging positive harmonic aliases.

The scope restriction matters. Lamzouri's Proposition 2.1 supplies a universal finite-multiset inequality for its special kernel, and WI-145--WI-150 study what would be required of a more general scalar profile if the same universal census inequality were retained. Actual zeta zeros form a highly restricted subset of conjugation-invariant configurations. A source-specific inequality valid only on realizable zeta configurations could evade the phase-mask probes; so could a matrix-valued, joint, nonlinear, or genuinely higher-correlation observable. Those are not failures of (38), but precisely the information discarded by the universal one-scalar abstraction.

## 6. Evidence provenance and prior-art audit

The zero-side input is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882 (submitted 2 September 2026), Proposition 2.1: <https://arxiv.org/abs/2609.02882>. Lamzouri proves the finite conjugation-invariant multiset inequality for `K=widehat(eta^2)`; the present argument uses the already-isolated Lamzouri-form abstraction (4), with `H` denoting the scalar kernel appearing in the census. The passage from integer multiplicities to (12), the phase-mask construction (13)--(25), and the resulting pointwise floor are exact deductions from that abstraction, not claims made in Lamzouri's paper.

The finite phase-mask optimization in Section 4 is a classical truncated trigonometric moment problem. A modern reference for the positive-semidefinite Toeplitz/Vandermonde characterization is Zai Yang and Lihua Xie, *Frequency-Selective Vandermonde Decomposition of Toeplitz Matrices with Applications*, arXiv:1605.02431: <https://arxiv.org/abs/1605.02431>. The endpoint computation (34)--(37) is elementary once that existence theorem is invoked.

The measure inequality (12) is naturally described as copositivity. General infinite-dimensional copositive-kernel frameworks exist, for example Cristian Dobre, Mirjam Duer, Leonhard Frerick and Frank Vallentin, *A copositive formulation for the stability number of infinite graphs*, arXiv:1305.1819: <https://arxiv.org/abs/1305.1819>, and Olga Kuryatnikova and Juan C. Vera, *Positive semidefinite approximations to the cone of copositive kernels*, arXiv:1812.00274: <https://arxiv.org/abs/1812.00274>. They supply context for the cone language, not this zeta-specific deduction.

The internal novelty audit compared WI-146--WI-150 and the earlier Bragg/alias findings WI-123 and WI-125. WI-150 contains the nearest collision but explicitly stops at the unmasked lattice sum and leaves harmonic repair open. A targeted external search around Lamzouri's new proof, Toeplitz/Caratheodory--Fejer phase masks, Fourier positivity, and copositive kernels found no direct statement of (6) or its derivation from Lamzouri-form bounded-depth universality. This is the novelty boundary used for persistence; **no claim of mathematical priority is made**.

## 7. Falsification boundary and next useful test

The result decisively closes one route, not the whole `weil_inertia` program. Under full scalar universality, a fixed negative spectral dip at radius `a>0` forces

\[
\phi(0)
\ge
\frac{-\phi(a)}{2}\cosh^2(2\pi Ba),
\tag{39}
\]

so a fixed-amplitude dip costs exponentially large central mass as `B` grows. The next useful falsification test is therefore no longer whether positive higher harmonics can repair the dip; they can be projected out. Instead, test whether the arithmetic normalization/prime-side constraints can permit the required growth of `phi_T(0)`, or whether a candidate improvement must abandon the universal scalar census and retain source-specific, matrix, or higher-correlation information.

No new unconditional zero proportion is claimed.