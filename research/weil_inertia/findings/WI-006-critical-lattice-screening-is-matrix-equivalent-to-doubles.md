# WI-006 — critical-lattice screening makes off-line pairs matrix-equivalent to on-line doubles

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `NEGATIVE/OBSTRUCTION`. The operator identity below is an exact consequence of the same Alpöge--Furman critical Gabor sampling and Poisson collapse used in WI-005. Painless/diagonal Gabor frame operators are classical, so no novelty is claimed for that harmonic-analysis mechanism. The new research consequence is sharper than WI-005: at critical vertical spacing, a lattice of simple off-line mirror pairs is not merely able to screen its negative inertia; it produces **exactly the same full compressed Weil operator** as a lattice of on-line double zeros at the same ordinates. Long finite clusters are asymptotically indistinguishable in trace norm, hence by every fixed spectral moment. This closes the proposed route of using a nonflat-window positive-spectrum remainder to distinguish screened off-line pairs from on-line doubles.

## 1. Question left open by WI-005

WI-005 showed that an isolated simple off-line pair

\[
\rho=\frac12+\delta+it,
\qquad
1-\bar\rho=\frac12-\delta+it
\]

has one positive and one negative direction in the Alpöge--Furman compressed Weil matrix, with negative magnitude increasing with the normalized horizontal depth `y=delta L`. It then showed that a vertical lattice at the critical spacing

\[
h=\frac{2\pi}{L}
\]

can screen this negative mass completely: the infinite aggregate becomes a positive multiplication operator independent of `delta`.

For the flat window the aggregate is `2I`, the equality shape of the rank--trace extremizer. For the Montgomery--Taylor window the same aggregate has a nontrivial positive spectral profile, with second moment per pair

\[
D_\psi=4\frac{\int\psi^2}{(\int\psi)^2}>4.
\]

That left a natural possibility: perhaps the negative mass is screened, but the residual positive-spectrum variance for a nonflat window can still tell a screened population of off-line pairs from on-line double zeros.

It cannot. The screened off-line operator is exactly the double-zero operator for **every** admissible Alpöge--Furman window at the critical sampling density.

## 2. The two zero configurations

Use the notation of WI-005 and Alpöge--Furman:

\[
L=\log(T/2\pi),
\qquad
h=\frac{2\pi}{L},
\qquad
\alpha_k=T+kh,
\qquad
a=\frac{\|\phi\|_2^2}{L},
\]

where `phi` is the real even taper supported in `[-L/2,L/2]`.

Put the vertical centers on the critical lattice

\[
t_j=t_0+jh,
\qquad j\in\mathbb Z.
\]

For a simple mirror pair at horizontal displacement `delta`, define

\[
w_j^{(\delta)}
:=\left(\widehat\phi(t_j-i\delta-\alpha_k)\right)_{k\in\mathbb Z}.
\]

Its normalized real-symmetric pair contribution is

\[
R_j^{(\delta)}
=\frac1{aL^2}
\left(
 w_j^{(\delta)}(w_j^{(\delta)})^{\mathsf T}
 +\overline{w_j^{(\delta)}}\,\overline{w_j^{(\delta)}}^{\mathsf T}
\right).
\tag{1}
\]

Now instead put an **on-line double zero** at the same ordinate `t_j`. With

\[
v_j:=w_j^{(0)}
=\left(\widehat\phi(t_j-\alpha_k)\right)_k
\in\ell^2(\mathbb Z;\mathbb R),
\]

multiplicity two gives

\[
D_j=\frac{2}{aL^2}v_jv_j^{\mathsf T}.
\tag{2}
\]

Thus

\[
\boxed{D_j=R_j^{(0)}}.
\tag{3}
\]

The question is whether the equality survives after replacing `delta=0` by a fixed nonzero horizontal displacement and summing over the critical vertical lattice.

## 3. Exact replacement identity on the full critical lattice

Take a finitely supported real coefficient vector `x=(x_k)` and write

\[
X(u)=\sum_kx_ke^{i\alpha_ku}.
\]

As in WI-005, if

\[
c_j^{(\delta)}(x)
=\sum_kx_k\widehat\phi(t_j-i\delta-\alpha_k),
\]

then

\[
x^{\mathsf T}R_j^{(\delta)}x
=\frac{2}{aL^2}\operatorname{Re}
\left(c_j^{(\delta)}(x)^2\right).
\tag{4}
\]

Expanding the two Fourier integrals in (4) and summing over `j` produces the factor

\[
\sum_{j\in\mathbb Z}e^{-ijh(u+v)}
=L\sum_{m\in\mathbb Z}\delta(u+v-mL).
\tag{5}
\]

Because `phi` is supported in an interval of length `L`, only the `m=0` term survives away from the vanishing taper endpoints. Hence `v=-u`. The horizontal displacement enters the double integral only through

\[
e^{-\delta(u+v)},
\]

and therefore on the surviving Poisson diagonal

\[
\boxed{e^{-\delta(u+v)}=1.}
\tag{6}
\]

Using evenness of `phi` and `X(-u)=\overline{X(u)}` for real `x` gives

\[
\sum_jx^{\mathsf T}R_j^{(\delta)}x
=\frac{2}{aL}\int_{-L/2}^{L/2}\phi(u)^2|X(u)|^2\,du.
\tag{7}
\]

But (7) is also the formula at `delta=0`, i.e. for the on-line doubles. Since both sides are real symmetric quadratic forms,

\[
\boxed{
\sum_{j\in\mathbb Z}R_j^{(\delta)}
=
\sum_{j\in\mathbb Z}D_j
\simeq
M_{\,2\phi^2/a}
\qquad\text{for every real }\delta.
}
\tag{8}
\]

This is an **operator identity**, not merely equality of trace, inertia, or the first two moments.

For the ideal flat window,

\[
M_{2\phi^2/a}=2I.
\]

For the Montgomery--Taylor or any other admissible nonflat window, both zero configurations produce the same nonconstant multiplier `2phi^2/a`.

## 4. The Montgomery--Taylor variance does not break the degeneracy

WI-005 computed that for a critical lattice the normalized second spectral moment per occupied center is

\[
D_\psi
=4\frac{\int_{-1/2}^{1/2}\psi(s)^2\,ds}
       {\left(\int_{-1/2}^{1/2}\psi(s)\,ds\right)^2},
\]

and in particular

\[
D_{\mathrm{MT}}=4.024508763\ldots.
\]

Equation (8) shows that this number is **not an off-line-depth signature**. Exactly the same multiplier and therefore exactly the same `D_psi` is produced by on-line doubles on the same lattice.

So the positive-spectrum variance term retained by WI-004 can detect that a nonflat screened block is not the flat equality operator `2I`, but it cannot determine whether the block came from

\[
\boxed{
\text{simple off-line mirror pairs}
\quad\text{or}\quad
\text{on-line double zeros}.
}
\]

This closes the second question posed at the end of WI-005 in its most direct form.

## 5. Long finite clusters inherit the equivalence

The full lattice is a local operator identity; a global zeta-like zero multiset cannot occupy every critical lattice site with a two-zero object because that would have twice the Riemann--von Mangoldt mean density. WI-005 therefore considered long occupied blocks separated by compensating gaps.

Let `J` be an interval of `M` consecutive critical-lattice centers and set

\[
Q_J^{(\delta)}=\sum_{j\in J}R_j^{(\delta)},
\qquad
D_J=\sum_{j\in J}D_j.
\]

For fixed normalized depth

\[
y=\delta L,
\]

WI-005 proved, with the same finite-section convention, that the off-line block differs from the positive compression of its infinite frame operator by

\[
\left\|Q_J^{(\delta)}-B_J\right\|_1
\ll_y \sqrt M+\log L.
\tag{9}
\]

At `delta=0` the same argument gives

\[
\left\|D_J-B_J\right\|_1
\ll \sqrt M+\log L,
\tag{10}
\]

and by (8) the reference operator `B_J` is the **same** in (9) and (10). Hence

\[
\boxed{
\left\|Q_J^{(\delta)}-D_J\right\|_1
\ll_y \sqrt M+\log L.
}
\tag{11}
\]

For the natural macroscopic blocks `M asymp L`,

\[
\boxed{
\frac1M\left\|Q_J^{(\delta)}-D_J\right\|_1\longrightarrow0.
}
\tag{12}
\]

The same remains true if different long blocks carry different bounded normalized depths `y_b`: the estimate is blockwise, and the boundary price is sublinear in each block. Choosing occupied and empty blocks with the appropriate duty cycle restores the global Riemann--von Mangoldt mean count while retaining an `o(N)` total replacement cost.

## 6. All fixed spectral moments are blind to the replacement

The trace-norm statement is stronger than the negative-mass screening of WI-005.

For fixed bounded `y`, the off-line block operators are uniformly bounded in operator norm. Indeed, from (4),

\[
\left|x^{\mathsf T}Q_J^{(\delta)}x\right|
\le
\frac{2}{aL^2}
\sum_{j\in J}|c_j^{(\delta)}(x)|^2,
\]

and the full critical Gabor family for the shifted window `phi(u)e^{-delta u}` has a Bessel bound depending only on the bounded normalized depth. The double-zero block has the corresponding `y=0` bound.

Therefore, for every fixed integer `r>=1`, telescoping powers and (11) give

\[
\left|
\operatorname{tr}\left((Q_J^{(\delta)})^r-D_J^r\right)
\right|
\le
rC_y^{r-1}\left\|Q_J^{(\delta)}-D_J\right\|_1
=o(M).
\tag{13}
\]

Thus

\[
\boxed{
\frac1M\operatorname{tr}(Q_J^{(\delta)})^r
-
\frac1M\operatorname{tr}D_J^r
\longrightarrow0
\qquad\text{for every fixed }r.
}
\tag{14}
\]

More generally, the standard Hermitian trace-norm eigenvalue inequality implies that the empirical spectral measures of the two finite blocks differ by `o(1)` against every fixed Lipschitz test function.

So adding third, fourth, or arbitrarily high **fixed** moments of the same single-scale critical Gabor compression does not by itself reveal whether such a screened exceptional block is off-line or double-on-line. A finite family of windows at the **same** critical bandwidth/grid is equally unable to break the replacement, because (8) holds window by window.

## 7. The zero-count ledger is also invariant under the replacement

The degeneracy is not only spectral.

In the Alpöge--Furman zero-side bookkeeping:

- one on-line double zero contributes multiplicity `2`, one distinct multiple critical point (`s_2 += 1`), and one positive-direction budget unit;
- one simple off-line mirror pair contributes two zeros, one off-line pair (`p += 1`), and one positive-direction budget unit.

Hence replacing a double by a simple mirror pair preserves

\[
N,
\qquad
s_2+p,
\qquad
\text{and the rank/inertia counting budget}.
\tag{15}
\]

Combined with (8)--(14), this gives a genuine replacement symmetry of the information used by the compressed-matrix method on a screened block:

\[
\boxed{
\text{critical-lattice doubles}
\ \longleftrightarrow\
\text{critical-lattice simple off-line pairs at fixed depth}
}
\]

up to a sublinear boundary cost for long finite clusters.

## 8. What this does and does not obstruct

This result does **not** refute a higher-moment or density-one theorem. A moment sequence can exclude an exceptional block because its **aggregate spectral distribution** is incompatible with the arithmetic moments, without ever deciding whether that block would have consisted of doubles or off-line pairs. In particular, the recent Yang--Yang density-one manuscript claims exactly such a route: the full moment tower is used to drive the allowed spectral mass at the origin to zero, and the same counting inequality then forces the total exceptional mass `s_2+p` to be `o(N)`.

What (8)--(15) rule out is a different hoped-for mechanism: **using more spectral information from the same single-scale critical Gabor compression to separate the two sources of exceptional mass once a screened configuration is present.** They are operator-equivalent in the bulk and count-equivalent in the zero ledger.

This sharpens the target for `weil_inertia`. To distinguish off-line pairs from doubles, or to charge horizontal displacement itself, some input must break the replacement symmetry. Plausible ways include:

- vertical information showing that actual zeta zeros cannot form long near-critical screening clusters;
- two-scale or cross-bandwidth test families, whose critical lattices cannot be simultaneously aligned;
- wider-support prime-side information / the `alpha>1` pair-correlation regime;
- a non-averaged or per-zero observable that retains horizontal depth before the Poisson diagonal erases it.

A merely richer polynomial functional of the **same** critical-band compressed matrix cannot do this job.

## 9. Prior art and novelty audit

The harmonic-analysis identity behind (8) is classical in kind.

- Alpöge--Furman supply the exact Poisson--Gabor identity for their critical-density test family and the zero-side hyperbolic block structure.
- Daubechies--Grossmann--Meyer and later painless/nonstationary Gabor-frame work explain why compact support plus critical/sufficiently dense modulation makes the frame operator diagonal or multiplicative.
- The standard trace-norm eigenvalue and polynomial perturbation inequalities used after (11) are classical matrix analysis.

A bounded literature search found no source applying that frame identity to identify a lattice of **off-critical Weil mirror-pair blocks** with the operator produced by **critical-line double zeros**. No novelty claim is made from absence of a search hit; the durable Mathia contribution is the exact consequence (8) and the resulting obstruction to a route explicitly left open by WI-005.

The recent Yang--Yang density-one manuscript is relevant as an audit target, not as established prior art: it uses the same critical Gabor compression and higher spectral moments, but its analytic transport remains `certified-candidate` pending external review, as already recorded in WI-002/WI-003 and `SOURCES.md`. The replacement identity does not contradict its logical architecture; it clarifies that any successful moment tower eliminates doubles and screened off-line pairs **together**, rather than learning which kind of exceptional zero produced a given screened block.

## 10. Consequence for the research program

The main zero-side degeneracy is now stronger than

\[
\text{multiplicity}\leftrightarrow\text{horizontal displacement}
\]

at the level of the first two moments. At critical sampling there is an explicit operator-level gauge:

\[
\boxed{
\text{on-line multiplicity two}
\quad\stackrel{\text{long critical-lattice block}}{\sim}\quad
\text{simple off-line mirror pair},
}
\]

where `~` means exact equality on the infinite screened lattice and `o(1)` normalized trace-norm difference on long finite blocks.

The next useful discriminator should therefore be tested against a permanent falsifier:

> **Double/off-line replacement test.** Take a long critical-lattice block of on-line doubles and replace it by simple mirror pairs at a fixed nonzero bounded normalized depth. Any proposed observable intended to distinguish the two exceptional populations must change by an order-one amount per zero. If its normalized change vanishes, it has not escaped the single-scale screening degeneracy.

This falsifier points directly toward cross-scale or genuinely vertical/arithmetic information rather than further single-scale spectral moments.