# AF-407 — Euler transform zero obstruction is continuation-only

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `TOTAL-POSITIVITY` · `LAPLACE-TRANSFORM` · `ANALYTIC-CONTINUATION` · `GAUGE-INVARIANT` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f(t):=-\log(1-e^{-e^t}),
\qquad
\Lambda_{a,b}(t):=e^{at+b}f(t),
\qquad a>0,\ b\in\mathbb R.
\tag{1}
\]

The exponential tilt in `(1)` is the same positive row/column gauge used in AF-217 and AF-406: it changes no finite translation-minor sign.

Its bilateral Laplace transform

\[
\mathcal B\Lambda_{a,b}(z)
:=\int_{-\infty}^{\infty}\Lambda_{a,b}(t)e^{-zt}\,dt
\tag{2}
\]

has the following exact structure.

1. The integral in `(2)` converges absolutely **exactly** on the half-plane

\[
\boxed{\Re z<a.}
\tag{3}
\]

2. On that genuine convergence domain,

\[
\boxed{
\mathcal B\Lambda_{a,b}(z)
=e^b\Gamma(a-z)\zeta(a-z+1),
}
\tag{4}
\]

and the transform is **zero-free throughout the whole half-plane** `(3)`.

3. Every nontrivial zeta zero `\rho=\beta+i\gamma`, `0<\beta<1`, produces a zero only after meromorphic continuation:

\[
\boxed{z_\rho=a+1-\rho,}
\tag{5}
\]

with

\[
\boxed{
\Re z_\rho-a=1-\beta>0.
}
\tag{6}
\]

Thus every nontrivial-zeta zero obstruction used in AF-217 lies strictly **beyond** the natural transform half-plane. Changing the admissible exponential gauge translates the convergence boundary and the continued zero pattern by the same amount; the offset `(6)` is gauge-invariant.

Consequently, the AF-217 all-order Pólya-frequency obstruction is not a zero already visible to the convergent Laplace integral. It is a **continuation-only obstruction**: all-order total positivity invokes Schoenberg's much stronger reciprocal-entire continuation law, and that global law is what collides with the nontrivial zeros.

This sharply limits one possible finite-order attack. Searching for zeros of `(2)` inside its actual convergence domain cannot falsify `TN_r` for any finite `r`, because there are no such zeros even before any total-positivity assumption is made. Any finite-order transform-zero theorem that is to constrain this Euler profile must use additional hypotheses capable of controlling continuation beyond `(3)`; compact-support theorems do this by making the transform entire, but that resource is absent here.

## Exact convergence domain

As `t\to-\infty`, `x=e^t\to0` and

\[
1-e^{-x}=x\left(1+O(x)\right),
\]

so

\[
f(t)=-\log(1-e^{-e^t})=-t+O(e^t).
\tag{7}
\]

Therefore the absolute value of the integrand in `(2)` has left-tail scale

\[
|t|e^{(a-\Re z)t}.
\tag{8}
\]

This is integrable at `-\infty` exactly when `a-\Re z>0`.

At `+\infty`,

\[
f(t)=e^{-e^t}\left(1+O(e^{-e^t})\right),
\tag{9}
\]

so the right tail is super-exponentially integrable for every complex `z`. Hence `(3)` is the exact absolute-convergence half-plane.

The boundary is not an artifact of a poor estimate. In the variable `w=a-z`, formula `(4)` has `w=0` at `z=a`; both `\Gamma(w)` and `\zeta(1+w)` have simple poles there, so the meromorphic continuation has a double pole at the transform boundary.

## Zero-free transform before continuation

For `\Re z<a`, put

\[
w=a-z,
\qquad \Re w>0.
\tag{10}
\]

Substituting `x=e^t` into `(2)` gives

\[
\begin{aligned}
\mathcal B\Lambda_{a,b}(z)
&=e^b\int_0^\infty x^{w-1}\bigl[-\log(1-e^{-x})\bigr]\,dx\\
&=e^b\Gamma(w)\zeta(w+1),
\end{aligned}
\tag{11}
\]

where the Euler-log expansion is absolutely summable because `\Re w>0`.

Now `\Gamma(w)` has no zeros, and

\[
\Re(w+1)>1.
\tag{12}
\]

The Euler product gives `\zeta(w+1)\neq0` in `(12)`. Therefore

\[
\boxed{
\mathcal B\Lambda_{a,b}(z)\neq0
\quad\text{for every }\Re z<a.
}
\tag{13}
\]

This zero-free statement uses no total positivity at all. It is already forced by the ordinary Euler-product half-plane.

## Where the zeta zeros enter

Let `\rho` be any nontrivial zero. The meromorphic continuation of `(11)` vanishes at `(5)` because

\[
a-z_\rho=\rho-1,
\qquad
\zeta(a-z_\rho+1)=\zeta(\rho)=0,
\tag{14}
\]

while `\Gamma(\rho-1)` is finite and nonzero. Since `0<\Re\rho<1`, equation `(6)` follows.

The functional-equation partner `1-\rho` gives the continued zero

\[
z_{1-\rho}=a+\rho,
\qquad
\Re z_{1-\rho}-a=\beta>0.
\tag{15}
\]

Thus a functional-equation pair sits beyond the convergence boundary at horizontal offsets `\beta` and `1-\beta`. The nearer offset is

\[
\min(\beta,1-\beta)>0,
\tag{16}
\]

and under RH both offsets would equal `1/2`. Nothing in this observation assumes RH; it only records exactly where the continued obstruction lives relative to the integral domain.

## Exponential-gauge invariance

AF-406 separates coefficient-sequence Pólya frequency from translation-kernel total positivity and shows that the profile gauge

\[
f(t)\mapsto e^{at+b}f(t)
\tag{17}
\]

rescales finite translation minors positively and leaves the normalized Toda certificates invariant.

The transform picture has the same rigidity. Replacing `a` by `a+c` moves the convergence wall from `\Re z<a` to

\[
\Re z<a+c,
\tag{18}
\]

while `(5)` moves every continued zeta zero from `a+1-\rho` to

\[
a+c+1-\rho.
\tag{19}
\]

Hence the relative displacement `(6)` is unchanged. No admissible positive exponential tilt can move a nontrivial zeta zero into the genuine convergence half-plane. This is the transform-side counterpart of AF-406's minor/Toda gauge invariance.

## Why AF-217 can still use those zeros

AF-217 assumes, for contradiction, all-order total nonnegativity. Schoenberg's `PF_\infty` theorem then upgrades the ordinary transform to

\[
\mathcal B\Lambda_{a,b}(z)=\frac1{\Psi(z)}
\tag{20}
\]

on the convergence domain, with `\Psi` an entire Laguerre--Pólya function. Equality with `(4)` on the open half-plane `(3)` forces equality of their meromorphic continuations. But `1/\Psi` cannot have a finite zero, whereas `(4)` continued meromorphically has the zeros `(5)`. That is the contradiction.

So the logical flow is not

\[
\text{finite transform already has a zeta zero}
\Longrightarrow
\text{total positivity fails}.
\]

It is instead

\[
PF_\infty
\Longrightarrow
\text{reciprocal-entire global continuation law}
\Longrightarrow
\text{continued transform cannot vanish}
\Longrightarrow
\text{contradiction with zeta zeros}.
\tag{21}
\]

The continuation law is the load-bearing resource.

## Finite-order prior-art boundary

Schoenberg's 1955 theory of multiply positive functions gives zero-exclusion results at finite order when extra analytic geometry is available. A modern strengthening by Apoorva Khare states, in particular, that if an integrable function is supported in an interval of length `\rho` and its translation kernel is `TN_p` on the required local domain, then its Fourier--Laplace transform is entire and zero-free in the strip

\[
|\Im s|<\frac{p\pi}{\rho}.
\tag{22}
\]

The compact-support width is essential data in that theorem: it makes the transform entire and sets the scale of the forbidden zero strip.

The tilted Euler profile `\Lambda_{a,b}` has support all of `\mathbb R` and the exact non-entire convergence geometry `(3)`. Therefore `(22)` cannot simply be imported to turn a nontrivial zeta zero into a finite-order contradiction. A localization or replacement theorem would first have to prove that the operation used to obtain a finite-width profile preserves the relevant `TN_p` information; merely truncating the source is not licensed by the existing argument.

This is consistent with the broader finite-order warning already isolated in AF-406. Katkova's work on **coefficient-sequence** `PF_m` for the Riemann xi function shows that finite multiple positivity can coexist with unchanged zero sets after suitable exponential coefficient gauges. That is a different representation category from the translation kernel here, but both examples show why finite positivity must be interpreted together with the exact representation and analytic resource that makes its zero theorem applicable.

## Arithmetic-fidelity consequence

The compression issue is now precise. The convergent transform

\[
\Lambda_{a,b}
\longmapsto
\mathcal B\Lambda_{a,b}|_{\Re z<a}
\tag{23}
\]

retains a zero-free analytic object. The nontrivial zeta-zero discriminator is not represented as a zero on that domain; it appears only in the uniquely determined meromorphic continuation beyond the transform wall. Exact mathematical continuation does not create new information, but **finite-order positivity tests confined to the native transform domain do not constrain that continued zero set by zero-freeness alone**.

For the current full-Euler translation-kernel frontier this rules out a seductive shortcut. AF-405 proves strict total positivity through order four, while AF-217 proves eventual finite-order failure. To locate the first failing order, one must still attack the actual finite-order structure -- for example the AF-404 Toda/confluent hierarchy -- or prove a new finite-order theorem that controls continuation for this noncompact profile. Merely inspecting zeros of `\Gamma(a-z)\zeta(a-z+1)` where the bilateral integral converges cannot distinguish order four, order five, or any other finite order.

## Prior-art and novelty audit

No novelty is claimed for the Mellin identity, Schoenberg's transform theorem, finite-order zero-exclusion theory, or the classical zero-free half-plane of zeta. The contribution is the exact representation-level boundary and its consequence for the current Arithmetic Fidelity frontier.

Relevant sources:

- I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* 1 (1951), 331--374, DOI `10.1007/BF02790092`. Role: reciprocal-entire Laplace-transform characterization for all-order Pólya-frequency functions used by AF-217.
- I. J. Schoenberg, **“On the Zeros of the Generating Functions of Multiply Positive Sequences and Functions,”** *Annals of Mathematics* 62(3) (1955), 447--471, DOI `10.2307/1970073`. Role: classical finite-order multiple-positivity / zero-location theory.
- Apoorva Khare, **“Multiply positive functions, critical exponent phenomena, and the Jain--Karlin--Schoenberg kernel,”** arXiv:`2008.05121`; published version associated with the 2020--2021 work. Role: Theorem D strengthens Schoenberg's compact-support finite-order transform zero-exclusion result and makes the support-width hypothesis explicit.
- Olga M. Katkova, **“Multiple positivity and the Riemann zeta-function,”** *Computational Methods and Function Theory* 7(1) (2007), arXiv:`math/0505174`, DOI `10.1007/BF03321628`. Role: direct prior art on finite `PF_m` phenomena for the xi coefficient sequence; representation-specific comparison already used in AF-406.

A targeted prior-art search found these established components but no need for a new general transform theorem. AF-407 should therefore be read as an exact **no-go on a particular finite-order strategy** and as a clarification of where AF-217's arithmetic discriminator survives the transform, not as a new theorem in total-positivity theory.

## Boundaries and falsification checks

- The claim concerns zeros of the **bilateral transform on its actual convergence domain** versus zeros of its meromorphic continuation. It does not say that finite-order total positivity has no consequences other than transform zero-freeness.
- The transform restriction `(23)` determines its analytic continuation uniquely when that continuation exists. “Continuation-only” therefore means that the obstruction is not a zero of the convergent integral, not that analytic continuation contains independent information.
- Compact-support finite-order theorems are not declared irrelevant. They identify an additional resource -- finite support width -- that the Euler profile lacks. A valid localization theorem preserving `TN_p` could make such results useful again.
- No statement is made about the smallest failing Euler order. AF-405 gives the current lower bound `m_fail>=5`; AF-217 gives existence of some finite failure; AF-407 does not narrow that numerical interval.
- No RH consequence is claimed. Equation `(6)` uses only the classical fact `0<\Re\rho<1` for nontrivial zeros.
- Trivial zeta zeros do not supply the same obstruction because the corresponding zeros of `\zeta(w+1)` are canceled by poles of `\Gamma(w)`, as already audited in AF-217.
- The exponential-gauge statement requires `a>0` when `\Lambda_{a,b}` itself is required to be integrable. The determinant-sign gauge identity exists more generally, but the `L^1` Pólya-frequency transform setup used here needs this admissibility condition.