# PC-335 — bounded indefinite radial forms cannot preserve semiprime nulls

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the bounded sign-changing/indefinite dilation-equivariant quadratic continuation left open by PC-185 and by the accepted signed-radial-flux clue.

PC-179 identifies the exact signed cyclotomic radial flux

\[
\rho_n(x)=-\frac{d}{dx}\log\Phi_n(e^{-x})
\]

and its Mellin transform

\[
\mathcal R_n(s)
=-\Gamma(s)\zeta(s)n^{1-s}
\prod_{p\mid n}(1-p^{s-1}).
\tag{1}
\]

PC-183--PC-185 show that positive refinement-covariant radial scalarizations cannot retain the exact prime-power selector, but PC-185 deliberately leaves a sign-changing or indefinite dilation-equivariant readout outside its positivity theorem. That escape can be closed for the full bounded quadratic multiplier class.

Fix any Mellin line `Re(s)=sigma>0`. Let `h in L^infty(R)` be real-valued; no sign condition is imposed. Define

\[
Q_{\sigma,h}(n)
:=\int_{\mathbb R}h(t)
\left|\mathcal R_n(\sigma+it)\right|^2dt.
\tag{2}
\]

The integral is finite because `rho_n` is bounded at the common vertex and decays exponentially, so Mellin-Plancherel places `mathcal R_n(sigma+it)` in `L^2(dt)` for every `sigma>0`.

The exact obstruction is:

\[
\boxed{
Q_{\sigma,h}(pq)=0\ \text{for every pair of distinct primes }p,q
\quad\Longrightarrow\quad
Q_{\sigma,h}(p^a)=0\ \text{for every prime power }p^a.
}
\tag{3}
\]

In fact, for each fixed prime `p` it is enough that the semiprime null hold for an unbounded sequence of distinct primes `q`. Thus allowing a bounded sign-changing Mellin symbol does not repair the Mangoldt selector: exact cancellation on the mixed-prime controls forces cancellation on the prime-power shell as well.

## 1. Separate the universal Mellin envelope from the radical factor

Put

\[
\alpha:=\sigma-1,
\qquad
W_\sigma(t):=
|\Gamma(\sigma+it)\zeta(\sigma+it)|^2,
\tag{4}
\]

and for every prime `p` define

\[
X_p(t):=|1-p^{\alpha+it}|^2
=1+p^{2\alpha}-2p^\alpha\cos(t\log p).
\tag{5}
\]

Taking absolute values in (1) gives, for a prime power `p^a`,

\[
\boxed{
|\mathcal R_{p^a}(\sigma+it)|^2
=p^{-2a\alpha}W_\sigma(t)X_p(t),
}
\tag{6}
\]

and for distinct primes `p,q`,

\[
\boxed{
|\mathcal R_{pq}(\sigma+it)|^2
=(pq)^{-2\alpha}W_\sigma(t)X_p(t)X_q(t).
}
\tag{7}
\]

At `sigma=1` the factor `W_1(t)` has the familiar zeta-pole singularity at `t=0`, but this causes no problem in the argument. For fixed `p`, equation (6) and Mellin-Plancherel show directly that

\[
h(t)W_\sigma(t)X_p(t)\in L^1(\mathbb R).
\tag{8}
\]

The Euler zero in `X_p` is exactly what cancels the pole when `sigma=1`.

Define the finite signed measure

\[
d\nu_p(t)
:=h(t)W_\sigma(t)X_p(t)\,dt
\tag{9}
\]

and its total mass

\[
A_p:=\nu_p(\mathbb R).
\tag{10}
\]

By (6),

\[
\boxed{
Q_{\sigma,h}(p^a)=p^{-2a\alpha}A_p.
}
\tag{11}
\]

Thus it remains only to show that semiprime nulls force `A_p=0`.

## 2. A large auxiliary prime forces the prime response to vanish

Assume `Q_{sigma,h}(pq)=0`. Since the scalar `(pq)^{-2alpha}` is nonzero, (7) gives

\[
0=\int_{\mathbb R}X_q(t)\,d\nu_p(t).
\tag{12}
\]

Using (5),

\[
\boxed{
(1+q^{2\alpha})A_p
=2q^\alpha\operatorname{Re}
\widehat\nu_p(\log q),
}
\tag{13}
\]

where

\[
\widehat\nu_p(u)
:=\int_{\mathbb R}e^{itu}\,d\nu_p(t).
\tag{14}
\]

Now let `q` tend to infinity through distinct primes for which the semiprime null is assumed.

If `alpha>0`, boundedness of the Fourier transform of a finite measure gives

\[
|A_p|
\le
\frac{2q^\alpha}{1+q^{2\alpha}}
\|\nu_p\|
=O(q^{-\alpha}),
\]

so `A_p=0`.

If `alpha<0`, equation (13) and the same bound give

\[
|A_p|
\le
\frac{2q^\alpha}{1+q^{2\alpha}}
\|\nu_p\|
\longrightarrow0,
\]

again forcing `A_p=0`.

The critical boundary `alpha=0`, i.e. `sigma=1`, is also rigid. Equation (13) becomes

\[
A_p=\operatorname{Re}\widehat\nu_p(\log q).
\tag{15}
\]

The measure `nu_p` has an `L^1` density by (8), so the Riemann--Lebesgue lemma gives

\[
\widehat\nu_p(\log q)\longrightarrow0.
\]

Hence `A_p=0` here as well. Substitution into (11) proves (3).

The proof uses neither positivity nor zero-freeness of the shell Mellin amplitude. The only ingredients are the exact radical factor in (1), boundedness of the readout, and the availability of arbitrarily large auxiliary prime controls.

## 3. The result removes the positivity hypothesis from the bounded one-carrier selector no-go

PC-185 proves that every fixed finite family of bounded shell-independent refinement-equivariant radial filters has Mellin fiber rank one. After the natural weight shift, the same statement applies to the signed flux: a finite filtered vector has the form

\[
\widehat J_n(t)
=\mathcal R_n(\sigma+it)m(t),
\tag{16}
\]

with a universal bounded vector of multiplier symbols `m(t)`.

Now let the final quadratic readout be any bounded Hermitian matrix multiplier `H(t)`, not necessarily positive semidefinite. Its diagonal shell response is

\[
\int
\widehat J_n(t)^*H(t)\widehat J_n(t)\,dt
=
\int h_{\mathrm{eff}}(t)
|\mathcal R_n(\sigma+it)|^2dt,
\tag{17}
\]

where

\[
h_{\mathrm{eff}}(t)=m(t)^*H(t)m(t)
\]

is real and bounded. Equation (3) therefore applies verbatim.

Consequently the positive-kernel obstruction of PC-185 was not an artifact of positivity for the exact selector question. **Within the bounded dilation-commutant and rank-one Mellin architecture, even an arbitrary sign-changing/indefinite Hermitian quadratic form cannot vanish on all semiprime shells while retaining any prime-power response.**

This is stronger than the pointwise argument used for positive forms. An indefinite symbol can certainly create cancellations on selected individual shells, but the full family of semiprime controls overdetermines those cancellations and forces the prime response to disappear.

## 4. Why the classical `Lambda` boundary is not a counterexample

PC-179 gives

\[
\mathcal R_n(1)=\Lambda(n).
\tag{18}
\]

That exact selector is point evaluation at the exceptional Mellin frequency `s=1`, produced by the pole-zero cancellation between `zeta(s)` and the cyclotomic Euler factors. It is not an `L^2` quadratic form with a bounded multiplier. In Mellin spectral language, extracting one frequency is distributional (`delta_{t=0}`), not a bounded multiplication readout.

PC-335 therefore sharpens the boundary rather than contradicting PC-179: regular bounded indefinite interior spectralization cannot preserve the Mangoldt nulls; the exact selector survives only in the singular endpoint/frequency channel already known to be the classical common-vertex identity.

## 5. Prior-art and novelty audit

The analytic ingredients are classical. Dilation-equivariant bounded operators becoming Mellin multipliers is the standard multiplicative harmonic-analysis framework already audited and sourced in PC-183--PC-185. The Riemann--Lebesgue lemma and the elementary expansion (5) are classical, and the cyclotomic Mellin factorization is PC-179's exact Ramanujan/zeta identity.

A directed literature check against scale-invariant Mellin operators, cyclotomic Mellin transforms, and prime-power selectors found the expected classical ingredients, not an independent RH mechanism of this form. No historical novelty is claimed for those ingredients, and no new external theorem is load-bearing; `SOURCES.md` therefore needs no new anchor.

The durable line-local delta is the **indefinite selector obstruction**: the positivity assumption left in PC-185 can be dropped if the required matched controls are the natural mixed-prime shells. The reason is arithmetic and exact, not convexity: the radical factor for an auxiliary prime `q` has only the three frequencies `0, +/-log q`, and its large-`q` scaling forces the one-prime moment to vanish.

## 6. Boundary and surviving frontier

The theorem applies to diagonal shell responses produced by bounded, shell-independent, refinement-equivariant linear filtering followed by a bounded Hermitian quadratic readout. It does not classify singular/distributional Mellin symbols, unbounded operators, genuinely shell-dependent kernels, non-scalar refinement cocycles, nonlinear radial operations, or operators that mix different shell labels before the final quadratic form.

Accordingly the accepted `cyclotomic-signed-radial-flux-assembly` clue remains open only beyond this bounded one-carrier quadratic class. In particular, a surviving sign-changing proposal must be genuinely cross-shell or singular/nonlinear; merely replacing the positive multiplier of PC-185 by an indefinite bounded one is now ruled out.

For the RH objective, this is a negative architecture theorem. It does not produce a functional equation, zero criterion, or critical-line positivity. It removes one of the most natural remaining ways to preserve the exact signed prime-power selector while staying inside the intrinsic radial refinement symmetry.

## Audit / falsification tests

The exact claim can be falsified by a bounded real symbol `h`, a line `sigma>0`, and one prime `p` such that `Q_{sigma,h}(pq)=0` along an unbounded sequence of distinct primes `q` while `Q_{sigma,h}(p^a) != 0` for some `a>=1`. Equations (12)--(15) exclude such an example.

The delicate case is `sigma=1`: one must verify that `h W_1 X_p` is integrable despite the zeta pole. This follows directly from (6), since it is a constant multiple of `h(t)|R_p(1+it)|^2`, and Mellin-Plancherel makes that integrable. Riemann--Lebesgue then gives the required limit.

Passing these tests establishes only the bounded quadratic no-go above. It does not rule out the singular common-vertex evaluation `R_n(1)=Lambda(n)` or a genuinely cross-shell signed assembly.