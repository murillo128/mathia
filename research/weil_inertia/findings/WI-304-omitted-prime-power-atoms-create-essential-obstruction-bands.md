# WI-304 — Omitted prime-power atoms create essential obstruction bands immune to compact repair

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`.

Vincent Liu's obstruction theorem at the pinned source commit in WI-302 uses the first post-localization prime power, `q=8`, to show that a particular tail-dropped comparison cannot be repaired by any fixed compact self-adjoint operator once `L>log(8)/2`. The source proof is more structural than that numerical specialization suggests. The same two-bump high-frequency construction gives, for every individually isolatable active prime-power atom, a whole interval in the **essential numerical range** of the tail-dropped comparison. The obstruction threshold is therefore not intrinsically `8`: it is a coefficient-versus-high-frequency-reserve condition.

This finding does not strengthen the accepted positivity aperture and does not validate Liu's unreplayed `17/16` certificate. It classifies what any future localization of the same type must preserve if it hopes to replace omitted arithmetic terms by compact corrections.

## 1. Source-exact setup

At Liu's frozen source commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`, the Weil form is normalized with

\[
c_n=\frac{2\Lambda(n)}{\sqrt n}.
\]

For the normalized localizer `chi`, put

\[
\rho_\chi(x)=\int \chi(v+x)\chi(v)\,dv.
\]

The source has `supp rho_chi subset (-2,2)`. Its localization defect is the bounded Hermitian form

\[
\begin{aligned}
\mathcal E_\chi(f)
={}&\int_0^{2L}(1-\rho_\chi(x))
\left(\frac{2e^{-x/2}}{1-e^{-2x}}-4\cosh(x/2)\right)H_f(x)\,dx\\
&+\sum_{\log n<2L}c_n(1-\rho_\chi(\log n))H_f(\log n).
\end{aligned}
\tag{1}
\]

The tail-dropped lower comparison is

\[
\mathcal D_\chi=\mathcal M_\chi-\mathcal E_\chi,
\]

where the localized comparison satisfies, on high-frequency modulations of a fixed compactly supported test,

\[
\frac{\mathcal M_\chi(f_k)}{\|f_k\|^2}\longrightarrow \beta_0,
\qquad \beta_0=\frac1{16}.
\tag{2}
\]

Liu proves (2) because the operator of `R_1-beta_0 I` is compact; the averaging in `M_chi` preserves the weakly-null high-frequency limit. The source then specializes (1) to `q=8`.

## 2. Atomwise essential-range theorem

Fix `L>0` and an integer `q>=2` with `Lambda(q)>0` and

\[
a:=\log q<2L.
\]

Assume the atom at `a` is **individually isolatable**: there is `d>0` such that two equal smooth bumps of radius `d`, centered at `+-a/2`, lie in `(-L,L)`, and the `2d`-neighborhood of `a` contains no other `log n` with `Lambda(n)>0`. For every fixed phase `theta in R`, choose a nonzero real bump pair `g` of this form and set

\[
T_k=\frac{2\pi k+\theta}{a},
\qquad
f_k(u)=e^{iT_k u}g(u).
\]

Then `f_k/||g||` is a weakly-null sequence of unit vectors. The autocorrelation of `g` is supported near `0,+-a`, and

\[
h_g(a)=\frac{\|g\|^2}{2}.
\]

Hence all discrete terms in (1) vanish except the `q` atom, while

\[
\frac{H_{f_k}(a)}{\|g\|^2}
=\frac12\cos\theta.
\tag{3}
\]

The continuous term in (1) tends to zero by the Riemann--Lebesgue lemma. Combining (1)--(3) with the high-frequency limit (2) gives the exact Rayleigh-quotient limit

\[
\boxed{
\lim_{k\to\infty}
\frac{\mathcal D_\chi(f_k)}{\|f_k\|^2}
=
\beta_0-w_q\cos\theta,
}
\tag{4}
\]

where

\[
\boxed{
w_q
=\frac{c_q}{2}\bigl(1-\rho_\chi(\log q)\bigr)
=\frac{\Lambda(q)}{\sqrt q}
\bigl(1-\rho_\chi(\log q)\bigr).
}
\tag{5}
\]

For bounded operators on a Hilbert space, the classical Fillmore--Stampfli--Williams characterization of the essential numerical range says that a limit of Rayleigh quotients along weakly-null unit vectors belongs to `W_e`. Varying `theta` in (4) therefore yields

\[
\boxed{
[\beta_0-w_q,\,\beta_0+w_q]
\subseteq W_e(\mathcal D_\chi).
}
\tag{6}
\]

Because the essential numerical range is invariant under compact perturbations, every compact self-adjoint `K` satisfies

\[
[\beta_0-w_q,\,\beta_0+w_q]
\subseteq W_e(\mathcal D_\chi+K).
\tag{7}
\]

Thus the exact atomwise obstruction criterion is

\[
\boxed{
w_q>\beta_0
\quad\Longrightarrow\quad
\mathcal D_\chi+K\not\succeq0
\text{ for every fixed compact self-adjoint }K.
}
\tag{8}
\]

The proof uses only the source-exact defect formula, geometric isolation of one atom, Riemann--Lebesgue, weak convergence of high-frequency modulations, and the classical compact-invariance theorem. No numerical spectral calculation enters.

## 3. Liu's `q=8` theorem is the first instance

For Liu's localizer, `rho_chi(x)=0` whenever `|x|>=2`. Therefore every isolatable prime power with `log q>2` has

\[
w_q=\frac{\Lambda(q)}{\sqrt q}.
\tag{9}
\]

At `q=8`,

\[
w_8=\frac{\log2}{2\sqrt2}>\frac1{16}=\beta_0.
\]

Taking `theta=0` in (4) gives exactly Liu's limiting defect

\[
\frac1{16}-\frac{\log2}{2\sqrt2}<0.
\]

The source proves this one phase and this one atom. Equation (6) shows that the same construction actually produces the full essential interval

\[
\left[
\frac1{16}-\frac{\log2}{2\sqrt2},
\frac1{16}+\frac{\log2}{2\sqrt2}
\right]
\subseteq W_e(\mathcal D_\chi).
\tag{10}
\]

So the obstruction is not merely a bad test vector: it is an essential, compact-invariant band in the bounded comparison operator.

## 4. Consequence for future tail-preserving architectures

The useful design rule is coefficient-based. Whenever a localization leaves an active, individually isolatable prime-power channel in its defect and that channel satisfies

\[
\frac{\Lambda(q)}{\sqrt q}
\bigl(1-\rho_\chi(\log q)\bigr)>\beta,
\tag{11}
\]

where `beta` is the comparison's high-frequency reserve, that omitted channel cannot be neutralized by any fixed compact correction. A successful architecture must instead change at least one of the ingredients visible in (11): retain source-exact noncompact information for the channel, raise the high-frequency reserve, choose a localizer with smaller `1-rho_chi`, or introduce some other noncompact term that survives the same weakly-null sequence.

This refines WI-303. WI-303 showed that Liu's rank-two extraction is not structurally necessary and that compact repair cannot replace the dropped noncompact tail. The present result identifies an exact local obstruction carried by each omitted arithmetic channel and explains what quantity a redesigned localization has to beat.

There are two important limits to the conclusion. First, (8) is a **necessary obstruction**, not a sufficient positivity criterion after all dangerous atoms are handled. Second, it does not prove that the entire infinite arithmetic tail must be retained. Since `Lambda(q)/sqrt(q) -> 0` along prime powers, the set satisfying (11) is finite for any fixed positive reserve once `rho_chi(log q)=0`. What is forced is noncompact information sufficient to neutralize every dangerous active channel, not literal retention of every prime-power term.

## 5. Prior-art and novelty audit

Liu's pinned manuscript gives the exact defect identity (1), the compactness/high-frequency argument (2), and the explicit `q=8`, `theta=0` obstruction. It does not state an arbitrary-prime-power coefficient criterion or identify the resulting essential numerical-range interval. The weakly-null characterization and compact invariance of `W_e` are classical operator theory, notably P. A. Fillmore, J. G. Stampfli and J. P. Williams, **On the essential numerical range, the essential spectrum, and a problem of Halmos**, *Acta Sci. Math. (Szeged)* 33 (1972), 179--192.

A targeted audit for compact-perturbation/Weyl-sequence formulations around Weil positivity and prime-power localization found Liu's `q=8` obstruction and general operator-theoretic essential-range references, but no matching source that states (4)--(11) as an atomwise Weil-form criterion. No priority claim is made. The Mathia contribution is the exact extraction of the coefficient-versus-reserve invariant and its essential-numerical-range formulation from Liu's source-exact mechanism.

### Primary sources

- Vincent Liu, **Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function**, frozen source in `luciferyu666/certified-weil-positivity`, commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`, especially the localization defect identity and Obstruction Theorem.
- P. A. Fillmore, J. G. Stampfli and J. P. Williams, **On the essential numerical range, the essential spectrum, and a problem of Halmos**, *Acta Sci. Math. (Szeged)* 33 (1972), 179--192.

### Validation boundary

The generalization is exact for the bounded tail-dropped comparison satisfying the stated source hypotheses and for individually isolatable active atoms. It does not assert negativity of the full Weil form, because the omitted source-exact positive remainder in `Q=D_chi+S_chi` can compensate the defect. It does not promote WI-302's `17/16` finite certificate, which remains at its existing independent-replay evidence boundary.