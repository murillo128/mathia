# NB-317 — Reduced-denominator shell coordinates make the Cesàro-to-primitive loss sharply N^(3/2)

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-315, NB-316
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + METHOD-BOUNDARY + FAREY-DENOMINATOR + CESARO-SHELL + CENTERED-PRIMITIVE + SHARPNESS-CONTROL + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\]

and use the reciprocal profile, reciprocal mean, centered profile, and centered primitive from `NB-315` and `NB-316`:

\[
F_u(t):=u(1/t),
\qquad
\widetilde F_u(t):=F_u(t)-\mu_N(u),
\qquad
G_u(T):=\int_0^T\widetilde F_u(s)\,ds.
\]

Let `Q_N^0(u)` be the centered Cesàro shell energy from `NB-315`, equivalently the squared `l^2` norm of the nonzero reciprocal-shell Fourier coefficients. Define the Cesàro-to-primitive amplification

\[
\mathcal A_N
:=
\sup_{0\ne u\in U_N}
\frac{\|G_u\|_\infty}{\sqrt{Q_N^0(u)}}.
\tag{1}
\]

Then the Farey-frequency system admits an exact reduced-denominator diagonalization. If

\[
u=\sum_{j=2}^N a_jg_j,
\qquad
B_q(u):=\sum_{\substack{2\le j\le N\\q\mid j}}\frac{a_j}{j}
=\sum_{1\le \ell\le N/q}\frac{a_{\ell q}}{\ell q},
\qquad 2\le q\le N,
\tag{2}
\]

then

\[
\boxed{
Q_N^0(u)
=
\sum_{q=2}^N W(q)|B_q(u)|^2,
}
\tag{3}
\]

where

\[
\boxed{
W(q)
:=
\sum_{\substack{1\le a<q\\(a,q)=1}}
\frac1{|1-e^{2\pi ia/q}|^2}
=
\frac{J_2(q)}{12}
=
\frac{q^2}{12}\prod_{p\mid q}\left(1-\frac1{p^2}\right).
}
\tag{4}
\]

At every integer `K>=0`, the primitive has the exact form

\[
\boxed{
G_u(K)
=-\sum_{q=2}^N B_q(u)D_q(K),
}
\tag{5}
\]

with

\[
D_q(K)
:=
\sum_{\substack{1\le a<q\\(a,q)=1}}
\frac{1-\cos(2\pi aK/q)}{|1-e^{2\pi ia/q}|^2}
\in[0,2W(q)].
\tag{6}
\]

Writing

\[
S_N:=\sum_{q=2}^N W(q)=\frac1{12}\sum_{q=2}^N J_2(q),
\tag{7}
\]

the exact evaluation norm in the `Q_N^0` metric is

\[
\boxed{
\mathcal A_N^2
=
\max_{0\le K<P_N}
\sum_{q=2}^N\frac{D_q(K)^2}{W(q)},
\qquad
P_N:=\operatorname{lcm}(2,\ldots,N),
}
\tag{8}
\]

and it satisfies the factor-two bracket

\[
\boxed{
\sqrt{S_N}
\le
\mathcal A_N
\le
2\sqrt{S_N}.
}
\tag{9}
\]

Since

\[
S_N
=
\frac{N^3}{36\zeta(3)}+O(N^2),
\tag{10}
\]

we obtain the sharp exponent

\[
\boxed{
\mathcal A_N=\Theta(N^{3/2}),
}
\tag{11}
\]

more explicitly,

\[
\left(\frac1{6\sqrt{\zeta(3)}}+o(1)\right)N^{3/2}
\le
\mathcal A_N
\le
\left(\frac1{3\sqrt{\zeta(3)}}+o(1)\right)N^{3/2}.
\tag{12}
\]

Thus the `N^(3/2)` frequency-to-primitive factor underlying `NB-315` is sharp in exponent when the input is measured by centered Cesàro shell energy. Regrouping the Farey frequencies by reduced denominator does reveal a much cleaner exact geometry, but it cannot by itself improve that exponent. Combined with `NB-316`, this isolates the remaining half-power window in the actual `L^2(0,1)` primitive amplification: any improvement of `Pi_N` below the `N^(5/2)` upper bound of `NB-315` must exploit the relation between `Q_N^0` and the Nyman Hilbert norm on primitive-extremizing profiles, or bypass the uniform primitive-supremum factorization altogether.

This is not an asymptotic for `Pi_N`, not a lower bound for the actual mixing error `||sqrt(m)T_(N,m)-R_N||`, not a lower bound for `beta_(N+1)(m)`, and not a target-occupation statement.

## 1. Reduced denominators diagonalize the centered shell spectrum

For a generator `g_j`, the reciprocal profile is constant on every unit cell `[k,k+1)` and has shell value

\[
r_j(k):=\frac{k\bmod j}{j}.
\tag{13}
\]

For a nonzero frequency `h/j`, the discrete Fourier coefficient of this `j`-periodic sawtooth is

\[
\widehat r_j(h/j)
=-\frac1{j(1-e^{-2\pi ih/j})}.
\tag{14}
\]

Now write a frequency in lowest terms as `a/q`, with `(a,q)=1` and `q>=2`. It occurs in the `j`-th generator exactly when `q|j`. Therefore the coefficient of `e^(2 pi i ak/q)` in the centered shell sequence of `u` is

\[
\boxed{
c_{a/q}(u)
=-\frac{B_q(u)}{1-e^{-2\pi ia/q}}.
}
\tag{15}
\]

All reduced frequencies with the same denominator are controlled by the single scalar `B_q(u)`.

The variables `B_2,...,B_N` are genuine coordinates rather than constrained summaries. If `x_j:=a_j/j`, then

\[
B_q=\sum_{\ell\le N/q}x_{\ell q},
\]

and finite Möbius inversion gives

\[
\boxed{
x_j=\sum_{\ell\le N/j}\mu(\ell)B_{j\ell}.}
\tag{16}
\]

Hence the map from generator coefficients to the reduced-denominator variables is triangular and invertible.

Parseval applied to the centered shell sequence now gives (3). To evaluate its denominator weight, use

\[
|1-e^{2\pi ia/q}|^2=4\sin^2(\pi a/q).
\]

The classical full-residue identity

\[
\sum_{a=1}^{r-1}\csc^2(\pi a/r)=\frac{r^2-1}{3}
\tag{17}
\]

and Möbius inclusion-exclusion over the gcd imply

\[
\sum_{\substack{1\le a<q\\(a,q)=1}}
\csc^2(\pi a/q)
=
\frac{q^2}{3}\prod_{p\mid q}\left(1-\frac1{p^2}\right).
\tag{18}
\]

Dividing by four yields (4).

## 2. Primitive evaluation is an exact diagonal dual problem

At an integer `K`, summing each nonzero Fourier mode from shell `0` through shell `K-1` gives

\[
G_u(K)
=
\sum_{q=2}^N\sum_{\substack{1\le a<q\\(a,q)=1}}
c_{a/q}(u)
\frac{1-e^{2\pi iaK/q}}{1-e^{2\pi ia/q}}.
\tag{19}
\]

Insert (15). Since

\[
(1-e^{-2\pi ia/q})(1-e^{2\pi ia/q})
=|1-e^{2\pi ia/q}|^2,
\]

and reduced residues pair as `a` and `q-a`, the imaginary parts cancel. This gives exactly (5)-(6). In particular, every `D_q(K)` is nonnegative and

\[
0\le D_q(K)\le2W(q).
\tag{20}
\]

Because the metric (3) is diagonal in the freely varying coordinates `B_q`, the dual norm of evaluation at a fixed integer `K` is exactly

\[
\sup_{0\ne u\in U_N}
\frac{|G_u(K)|^2}{Q_N^0(u)}
=
\boxed{
\sum_{q=2}^N\frac{D_q(K)^2}{W(q)}.
}
\tag{21}
\]

The centered reciprocal profile is constant on unit cells, so `G_u` is affine on each cell and the maximum of `|G_u|` on that cell is attained at an endpoint. It is also `P_N`-periodic because the centered profile has zero mean over the common period. Therefore the global supremum is attained at one of the integers `0,...,P_N-1`, proving (8).

## 3. Averaging over one common period makes the N^(3/2) exponent sharp

The upper bound in (9) follows immediately from (20):

\[
\sum_{q=2}^N\frac{D_q(K)^2}{W(q)}
\le
4\sum_{q=2}^NW(q)
=4S_N.
\tag{22}
\]

For the converse, average `K` uniformly over `0,...,P_N-1`. Because every `q<=N` divides `P_N`, the residue `K mod q` is uniform. For every nonzero reduced frequency,

\[
\mathbb E_K\cos(2\pi aK/q)=0,
\]

so

\[
\boxed{\mathbb E_KD_q(K)=W(q).}
\tag{23}
\]

Jensen then gives

\[
\mathbb E_KD_q(K)^2\ge W(q)^2.
\]

Averaging (21) therefore yields

\[
\mathbb E_K
\sum_{q=2}^N\frac{D_q(K)^2}{W(q)}
\ge
\sum_{q=2}^NW(q)
=S_N.
\tag{24}
\]

At least one integer `K` attains the right-hand side, proving the lower bound in (9). Notice that the common period is used only as a finite averaging device in this lower-bound proof; the magnitude of `P_N` never enters the estimate.

## 4. The denominator weight has cubic total mass

Equation (4) identifies `12W(q)` with the Jordan totient `J_2(q)`. Using

\[
J_2(q)=q^2\sum_{d\mid q}\frac{\mu(d)}{d^2},
\]

we obtain

\[
S_N+\frac1{12}
=
\frac1{12}\sum_{q\le N}J_2(q)
=
\frac1{12}\sum_{d\le N}\mu(d)
\sum_{r\le N/d}r^2.
\tag{25}
\]

Since

\[
\sum_{r\le X}r^2=\frac{X^3}{3}+O(X^2),
\]

we get

\[
S_N+\frac1{12}
=
\frac{N^3}{36}
\sum_{d\le N}\frac{\mu(d)}{d^3}
+O\left(N^2\sum_{d\le N}\frac1{d^2}\right)
=
\frac{N^3}{36\zeta(3)}+O(N^2),
\tag{26}
\]

which proves (10)-(12).

## 5. What this closes — and what it leaves open

`NB-315` factors the moving rank-one mixing bound through two uniform estimates:

\[
\|G_u\|_\infty
\lesssim
N^{3/2}\sqrt{Q_N^0(u)},
\qquad
\sqrt{Q_N^0(u)}\lesssim N\|u\|_2.
\tag{27}
\]

The first factor was previously obtained by Cauchy--Schwarz over individual Farey frequencies. Equations (3)-(12) show that its `N^(3/2)` exponent is intrinsic to the exact centered-shell Cesàro metric: even after all frequencies with the same reduced denominator are grouped and their common coefficient is used exactly, the optimal uniform constant still grows like `N^(3/2)`.

That narrows the method frontier left by `NB-316`. The actual Hilbert-normalized primitive amplification satisfies

\[
\Pi_N
\gtrsim
\frac{N^2}{\sqrt{\log N}}
\]

from the adjacent witness of `NB-316`, while `NB-315` still gives `Pi_N=O(N^(5/2))`. The remaining half-power gap cannot be closed by improving only the Farey-frequency-to-primitive step relative to `Q_N^0`; it must come from a stronger joint relation between primitive-large denominator profiles and the physical `L^2(0,1)` norm, or from an estimate of the weighted mixing integral that does not pass through `||G_u||_infinity`.

This result does not show that `Pi_N` is of order `N^(5/2)`: the profiles that extremize (1) may have much larger Hilbert norm than the worst-case comparison `Q_N^0(u) <= O(N^2)||u||_2^2` allows. It likewise says nothing by itself about target occupation, first-free gain, or RH.

## 6. Prior-art audit

A fresh search of the neighboring Nyman--Beurling Fourier/Gram literature and of classical fractional-part Fourier identities found the expected ingredients: finite Fourier expansions of periodic sawtooths, reduced-residue/Ramanujan-type grouping, and classical trigonometric sums such as (17). The reviewed Nyman--Beurling sources include the recent Gram analysis of Ehm and Fourier-based estimates of Maier--Rassias. I did not identify in the material reviewed a statement of the exact finite-section reduced-denominator diagonalization (3)-(8), nor the resulting sharp `Theta(N^(3/2))` Cesàro-to-primitive amplification. This is an audit result, not a claim of bibliographic novelty.

No external result beyond standard finite Fourier algebra, Möbius inversion, and the elementary trigonometric identity (17) is load-bearing for the proof, so `SOURCES.md` does not require a new dependency.
