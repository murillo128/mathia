# PC-147 — top-band projector is uniformly operator-local in chord radius

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY`. PC-143 proves that the isolated gap-two top band of the primorial primitive-shell inverse-square chord Laplacian does **not** converge to the exact gap-two matching space in operator norm, even though it does lock on average. PC-145 and PC-146 then show that bounded or growing chord windows recover the same top-band projector at the Mertens-scaled Frobenius level.

There is a stronger conclusion. The full isolated top-band projector itself is uniformly approximable in **operator norm** by finite chord-radius truncations. Moreover, the explicit operator-norm nonlocking obstruction of PC-143 already survives in every truncation containing the fixed chord offsets `4` and `6`. Thus long chords are not a hidden carrier of the sparse worst-angle defect: the defect is already finite-local, while the effect of all chords beyond radius `H` on the top-band subspace is `O(1/H)` uniformly in the primorial conductor.

## 1. Setup

Let

\[
N_x=\prod_{p\le x}p,
\qquad
L_x=\beta_{N_x}P_x+R_x
\]

be the primitive-shell inverse-square chord Laplacian and exact gap-two matching decomposition of PC-142--PC-146, with

\[
\beta_N=\frac1{2\sin^2(2\pi/N)},
\qquad
\operatorname{rank}P_x=E_x.
\]

For an integer cutoff `H>=3`, let `R_x^(H)` retain only the nonmatching primitive edges of symmetric cyclic distance at most `H`, and put

\[
L_x^{(H)}=\beta_{N_x}P_x+R_x^{(H)},
\qquad
T_x^{(H)}=R_x-R_x^{(H)}\succeq0.
\tag{1}
\]

Let `Q_x` be the spectral projector of `L_x` onto its isolated rank-`E_x` top band, and let `Q_x^(H)` be the corresponding top-band projector of `L_x^(H)`. PC-142 and PC-145 show that both bands have exactly rank `E_x` and are separated from their complementary spectra by

\[
\delta_{N_x}:=\beta_{N_x}-\rho_{N_x}>c_6N_x^2,
\qquad
c_6=\frac1{4\pi^2}-\frac5{216}>0.
\tag{2}
\]

PC-145 also gives the arithmetic-free long-chord tail estimate

\[
\boxed{
\|T_x^{(H)}\|\le a_HN_x^2,
\qquad
a_H:=\frac14\sum_{h>H}\frac1{h^2}.
}
\tag{3}
\]

Since `sum_{h>H}h^{-2}<=H^{-1}`,

\[
a_H\le\frac1{4H}.
\tag{4}
\]

When `H>=N_x/2`, the truncation is already the full operator and every estimate below is trivial.

## 2. Sylvester comparison gives an operator-norm bound

Set

\[
Q=Q_x,
\qquad Q_H=Q_x^{(H)},
\qquad T=T_x^{(H)},
\qquad X=(I-Q)Q_H.
\]

As in PC-145, define the complementary/full and selected/truncated restrictions

\[
L_-=(I-Q)L_x(I-Q),
\qquad
L_{H,+}=Q_HL_x^{(H)}Q_H.
\]

Because `Q` commutes with `L_x`, `Q_H` commutes with `L_x^(H)`, and `L_x=L_x^(H)+T`, direct multiplication gives the exact Sylvester equation

\[
\boxed{
L_-X-XL_{H,+}=(I-Q)TQ_H.
}
\tag{5}
\]

The spectrum of `L_-` lies at or below `rho_{N_x}`, while the spectrum of `L_{H,+}` lies at or above `beta_{N_x}`. The standard self-adjoint Sylvester/Davis--Kahan separation estimate therefore applies in operator norm:

\[
\|X\|
\le
\frac{\|(I-Q)TQ_H\|}{\delta_{N_x}}
\le
\frac{\|T\|}{\delta_{N_x}}.
\tag{6}
\]

Since `Q` and `Q_H` are equal-rank orthogonal projections, their operator distance is the largest sine of their principal angles and satisfies

\[
\|Q-Q_H\|=\|(I-Q)Q_H\|=\|X\|.
\tag{7}
\]

Combining (2), (3), and (7) gives the uniform estimate

\[
\boxed{
\|Q_x-Q_x^{(H)}\|
\le
\frac{a_H}{c_6}
\le
\frac1{4c_6H}.
}
\tag{8}
\]

No sieve average, Mertens factor, or Frobenius normalization is needed. In particular,

\[
\boxed{
\lim_{H\to\infty}
\sup_{x\ge5}
\|Q_x-Q_x^{(H)}\|=0,
}
\tag{9}
\]

where the supremum ranges over the primorial levels under discussion. More generally, for every integer sequence `H_x->infinity`, however slowly,

\[
\boxed{
\|Q_x-Q_x^{(H_x)}\|\longrightarrow0.
}
\tag{10}
\]

Thus the order-of-limits issue closed at Mertens/Frobenius scale by PC-146 is absent even in the strongest principal-angle topology: summability of the inverse-square chord tail plus the PC-142 macroscopic cliff already forces uniform operator locality.

## 3. The PC-143 nonlocking obstruction is already radius-six local

Operator locality of the **top-band projector** must not be confused with operator-norm locking of that band to the exact gap-two matching space. The latter remains false for a completely local reason.

For every primorial `N_x` with `x>=5`, PC-143 uses CRT to choose a residue `a` such that

\[
a\equiv5\pmod6,
\qquad
a\equiv2\pmod p\quad(5\le p\le x).
\tag{11}
\]

Then `a`, `a+2`, and `c=a+6` are primitive, `{a,a+2}` is a gap-two matching edge, and `c` is unmatched. Put

\[
u=\frac{e_a-e_{a+2}}{\sqrt2}\in\operatorname{ran}P_x.
\]

For every cutoff `H>=6`, both nonmatching edges from `c` to the support of `u` remain in `L_x^(H)`: their cyclic gaps are `6` and `4`. Since the `c` coordinate is untouched by projection onto the matching space,

\[
\left|
\left\langle e_c,
(I-P_x)L_x^{(H)}P_xu
\right\rangle
\right|
=
\frac{w_4(N_x)-w_6(N_x)}{\sqrt2},
\tag{12}
\]

where

\[
w_h(N)=\frac1{4\sin^2(\pi h/N)}.
\]

Hence, with

\[
B_{x,H}:=(I-P_x)L_x^{(H)}P_x,
\]

\[
\|B_{x,H}\|
\ge
\frac{w_4(N_x)-w_6(N_x)}{\sqrt2}.
\tag{13}
\]

The truncated primitive operator is an edge-subgraph compression of the full regular-polygon inverse-square Laplacian, whose norm is `N_x^2/8` for even `N_x`. Therefore

\[
\|L_x^{(H)}\|\le\frac{N_x^2}{8}.
\tag{14}
\]

Because `Q_x^(H)` is a spectral projector of `L_x^(H)`, it commutes with `L_x^(H)`. Exactly as in PC-143,

\[
B_{x,H}
=(I-P_x)[L_x^{(H)},P_x-Q_x^{(H)}]P_x,
\]

and consequently

\[
\|B_{x,H}\|
\le
2\|L_x^{(H)}\|\,\|P_x-Q_x^{(H)}\|.
\tag{15}
\]

Equations (13)--(15) imply, for every `H>=6`,

\[
\boxed{
\|P_x-Q_x^{(H)}\|
\ge
\frac{4\bigl(w_4(N_x)-w_6(N_x)\bigr)}{\sqrt2\,N_x^2}.
}
\tag{16}
\]

Using

\[
\frac{w_k(N)}{N^2}\longrightarrow\frac1{4\pi^2k^2}
\]

for fixed `k`, one obtains the same explicit obstruction as for the full projector:

\[
\boxed{
\liminf_{x\to\infty}
\|P_x-Q_x^{(H)}\|
\ge
\frac5{144\sqrt2\,\pi^2}
=0.00248767\ldots
\qquad(H\ge6\text{ fixed}).
}
\tag{17}
\]

Thus the sparse worst-angle defect does not need long chords at all. It is already present in a radius-six truncation, even though increasing finite radii approximate the **full** top-band projector uniformly by (9).

## 4. What the two operator-norm statements mean together

The exact boundary is now sharper than the Frobenius statements of PC-143--PC-146:

\[
\boxed{
Q_x^{(H)}\xrightarrow[H\to\infty]{\ \text{uniformly in }x\ }Q_x
\quad\text{in operator norm},
}
\tag{18}
\]

while for every fixed `H>=6`,

\[
\boxed{
P_x\not\to Q_x^{(H)}
\quad\text{in operator norm as }x\to\infty.
}
\tag{19}
\]

There is therefore no contradiction between PC-143's persistent worst principal angle and finite-radius locality. The relevant distinction is **locality of the actual spectral band** versus **collapse of that band onto the pure gap-two matching model**. The spectral band is uniformly localizable; the matching model is still missing bounded local interactions, already at offsets `4` and `6`.

This closes a natural escape route left after the Mertens-scale analysis: long chords cannot coherently rotate a sparse subspace by an order-one angle while remaining invisible to normalized Frobenius mass. Their total effect on the selected top-band subspace is uniformly bounded by the summable tail in (8). Any unexplained operator-scale organization in this band must already be generated inside sufficiently large but finite chord windows, or else enter through observables not controlled by the isolated projector itself, such as internal band spacings or cross-level transport.

## 5. Prior-art and novelty audit

The abstract perturbation step is classical. Chandler Davis and W. M. Kahan, **The Rotation of Eigenvectors by a Perturbation. III**, *SIAM Journal on Numerical Analysis* 7 (1970), 1--46, DOI `10.1137/0707001`, is the standard source for eigenspace rotation under separated self-adjoint spectra and is already anchored for PC-143/PC-145 in `research/prime_circle/SOURCES.md`. Modern semidefinite variants of the same subspace-perturbation problem likewise bound spectral-projection motion by perturbation norm relative to the spectral separation.

A directed search across spectral-projector perturbation, long-range graph-Laplacian truncation, reduced-residue Laplacians, and inverse-square chord operators did not locate this exact Prime-Circle specialization. That absence is not evidence of historical priority, and no novelty is claimed for Davis--Kahan/Sylvester theory, graph-Laplacian norm monotonicity, or the summable `1/h^2` tail. The durable result is the exact combination of the already-persisted PC-142 cliff, PC-145 tail estimate, and PC-143 CRT obstruction: **uniform operator-locality of the actual top band coexists with a fixed finite-local obstruction to matching-space locking**.

The RH audit is negative. Equations (8)--(17) use only the inverse-square chord decay, the elementary period-six spectral cliff, finite CRT, and classical perturbation theory. No analytic continuation, functional equation, gamma factor, zeta-zero divisor, or critical-line symmetry appears. This is therefore a localization/classicalization boundary, not a new RH mechanism.

## 6. Boundary and falsification surface

The operator-locality theorem depends on the exact isolated-band statement of PC-142/PC-145. If the full and truncated selected bands did not have the same rank or a common `c_6N_x^2` separation from their complements, the equal-rank projection identity (7) or the Sylvester estimate (6) would have to be re-audited.

The quantitative constant `1/(4c_6H)` is not claimed sharp. It uses only the soft tail bound `sum_{h>H}h^{-2}<=1/H`; sharper control of the discarded chord degree could improve the rate without changing the conclusion.

The lower bound (17) is asserted only for cutoffs `H>=6`, because its explicit witness uses precisely the offsets `4` and `6`. It proves persistence of one sparse finite-local defect, not a classification of all exceptional directions.

Finally, (9) controls the isolated top-band **subspace**. It does not classify eigenvalue spacings or eigenvector organization *inside* that band, nonlinear observables built from the finite windows, or transport of those internal structures across refinement levels. Those remain outside this operator-locality boundary.