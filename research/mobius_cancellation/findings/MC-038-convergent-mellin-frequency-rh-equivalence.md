# MC-038 — Convergent endpoint Mellin frequencies remain RH-equivalent on the Huxley–Watt annulus

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/BOUNDARY`, `RH-EQUIVALENT-BOUNDARY`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-036` proved that every **fixed** Mellin character of the exact Huxley–Watt product annulus carries an RH-equivalent critical-scale estimate, but deliberately left open the finite-log-interval Fourier frequencies

\[
\tau_N=\frac{2\pi k_N}{\log N},
\]

because these vary with the outer scale `N`. A large part of that apparent escape can in fact be closed without any new zeta input.

Let `(\tau_N)_{N\ge2}` be any real sequence converging to a finite limit `\tau_*`, and define

\[
F_{\tau_N}(N):=\sum_{n\le N}\mu(n)n^{-i\tau_N}.
\tag{1}
\]

Then

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
F_{\tau_N}(N)=O_\varepsilon(N^{1/2+\varepsilon})
\ \text{for every }\varepsilon>0.
}
\tag{2}
\]

The converse direction does **not** require a uniform estimate for one fixed twist at all smaller scales. The endpoint-dependent twist can be untwisted by a self-absorbing Abel-summation inequality around its limiting character.

Retain the finite-cutoff product coefficient from `MC-032`–`MC-036`,

\[
c_N(q)=\sum_{\substack{mn=q\\m,n\le N}}\mu(m)\mu(n),
\tag{3}
\]

and define the corresponding scale-dependent annular Mellin mode

\[
T_{\tau_N}(N)
:=
\sum_{N<q\le N^2}
 c_N(q)
\left(\frac{N^2}{q}\right)^{i\tau_N}.
\tag{4}
\]

The pointwise factorization from `MC-036` is valid for every real frequency separately, hence also after substituting `\tau=\tau_N`:

\[
T_{\tau_N}(N)
=N^{2i\tau_N}
\left(F_{\tau_N}(N)^2-G_{\tau_N}(N)\right),
\tag{5}
\]

where

\[
G_{\tau_N}(N)
:=\sum_{q\le N}(\mu*\mu)(q)q^{-i\tau_N}
\quad\text{satisfies}\quad
|G_{\tau_N}(N)|=O(N\log N)
\tag{6}
\]

uniformly in the frequency. Consequently

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
T_{\tau_N}(N)=O_\varepsilon(N^{1+\varepsilon})
\ \text{for every }\varepsilon>0
}
\tag{7}
\]

for **every convergent real frequency schedule** `(\tau_N)`.

For the natural Fourier basis on the finite log-radial interval `0<=u<=log N`, this has an immediate consequence. If

\[
\frac{k_N}{\log N}\longrightarrow \kappa
\tag{8}
\]

for any finite real `\kappa`, then `\tau_N=2\pi k_N/\log N -> 2\pi\kappa`, so the critical estimate for that individual scale-dependent mode is already equivalent to RH. In particular, this kills the scalar escape for every fixed Fourier index, every `k_N=o(log N)`, and every asymptotically linear index `k_N=\kappa\log N+o(log N)`.

The surviving harmonic opportunity is therefore narrower than `MC-036` left open: it must use genuinely **nonconvergent/high-frequency schedules**, coupled cancellation among modes before absolute values, or an arithmetic production mechanism that controls the coarse/fixed-frequency content from independently weaker information. Merely allowing the Mellin frequency to drift with `N` does not make a convergent mode cheaper.

## 1. A varying endpoint twist can be untwisted around its limit

Write

\[
\delta_N:=\tau_N-\tau_*\longrightarrow0
\tag{9}
\]

and freeze the limiting character into the coefficients

\[
a_n:=\mu(n)n^{-i\tau_*},
\qquad
A(x):=\sum_{n\le x}a_n=F_{\tau_*}(x).
\tag{10}
\]

Then the endpoint-dependent sum is

\[
F_{\tau_N}(N)
=\sum_{n\le N}a_n n^{-i\delta_N}.
\tag{11}
\]

For each fixed endpoint `N`, `\delta_N` is just a constant. Abel summation therefore gives the exact identity

\[
F_{\tau_N}(N)
=N^{-i\delta_N}A(N)
+i\delta_N\int_1^N A(u)u^{-i\delta_N-1}\,du.
\tag{12}
\]

Hence

\[
|A(N)|
\le
|F_{\tau_N}(N)|
+|\delta_N|\int_1^N\frac{|A(u)|}{u}\,du.
\tag{13}
\]

This is the decisive point: the error coefficient tends to zero. The phase does not have to be compared term-by-term with the limiting phase, which would lose a factor of order `N|\delta_N|\log N`; instead the difference is fed through the **already accumulated partial sum** `A(u)`.

Assume now the right side of (2). Fix any

\[
\alpha>\frac12.
\tag{14}
\]

Using the hypothesis with `\varepsilon=\alpha-1/2`, there is a constant `C_\alpha` such that

\[
|F_{\tau_N}(N)|\le C_\alpha N^\alpha
\tag{15}
\]

for all sufficiently large `N`. Since `\delta_N->0`, choose `N_0` so that

\[
|\delta_N|\le \frac\alpha2
\qquad(N\ge N_0).
\tag{16}
\]

Extend the endpoint schedule piecewise constantly between integers; this does not change any partial sum and allows the same inequality for real endpoints up to harmless bounded factors. For `X>=N_0`, put

\[
B(X):=\sup_{N_0\le x\le X}\frac{|A(x)|}{x^\alpha}.
\tag{17}
\]

Splitting the integral in (13) at `N_0` and using the definition of `B(X)` on the upper part gives, uniformly for `N_0<=x<=X`,

\[
\frac{|A(x)|}{x^\alpha}
\le
C_\alpha+C_{N_0,\alpha}
+\frac{|\delta_x|}{\alpha}B(X).
\tag{18}
\]

After increasing `N_0` once more if necessary, the last coefficient is at most `1/2`. Taking the supremum yields

\[
B(X)
\le
C_\alpha+C_{N_0,\alpha}+\frac12 B(X),
\tag{19}
\]

so `B(X)` is bounded independently of `X`. Therefore

\[
F_{\tau_*}(x)=A(x)=O_\alpha(x^\alpha)
\tag{20}
\]

for every `\alpha>1/2`.

`MC-036` already proves that a fixed twist has the same critical exponent as the ordinary Mertens function by two-way partial summation. Thus (20) for every `\alpha>1/2` implies

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\tag{21}
\]

for every positive `\varepsilon`, and the classical Littlewood–Titchmarsh Mertens criterion gives RH.

This proves the nontrivial direction of (2).

## 2. RH controls every convergent schedule uniformly enough

Assume RH. For every positive `\eta`, the classical Mertens criterion gives

\[
M(x)=O_\eta(x^{1/2+\eta}).
\tag{22}
\]

Because a convergent frequency schedule is bounded, ordinary partial summation with the frozen endpoint frequency gives

\[
\begin{aligned}
|F_{\tau_N}(N)|
&\le |M(N)|
+|\tau_N|\int_1^N\frac{|M(u)|}{u}\,du\\
&=O_\eta(N^{1/2+\eta})
\end{aligned}
\tag{23}
\]

with a constant depending only on `\eta` and the bounded frequency range. Choosing `\eta` smaller than the requested exponent proves the forward implication in (2).

No analytic continuation of `1/zeta(s)` is used in the transfer between the variable and limiting twists. The only RH input in this direction is the classical Mertens criterion itself.

## 3. The annular statement follows without another loss

Equation (5) is the exact finite identity of `MC-036` evaluated at the frequency `\tau_N`. The interior estimate (6) is uniform because it is obtained by absolute values:

\[
|G_{\tau_N}(N)|
\le
\sum_{q\le N}|(\mu*\mu)(q)|
=O(N\log N).
\tag{24}
\]

If RH holds, (2) and (5)–(6) give

\[
T_{\tau_N}(N)=O_\varepsilon(N^{1+\varepsilon})
\tag{25}
\]

for every positive `\varepsilon`.

Conversely, assume (25). Then

\[
|F_{\tau_N}(N)|^2
\le
|T_{\tau_N}(N)|+|G_{\tau_N}(N)|
\ll_\varepsilon N^{1+\varepsilon}+N\log N.
\tag{26}
\]

Using a smaller auxiliary exponent and taking square roots gives the critical bound in (2), hence RH by Section 1. This proves (7).

Thus the scale-dependent annular mode does not acquire a weaker information budget merely because its character changes from one outer scale to the next, provided those characters converge.

## 4. Consequence for finite-interval log Fourier modes

The natural orthogonal characters on the interval `0<=u<=L`, `L=log N`, are

\[
e^{2\pi i k u/L},
\tag{27}
\]

which correspond to physical Mellin frequencies

\[
\tau_N=\frac{2\pi k_N}{\log N}.
\tag{28}
\]

`MC-036` correctly noted that a fixed Fourier index `k` produces a varying physical frequency and therefore was not covered by its fixed-`\tau` proof. Equations (2) and (7) now close exactly that gap.

More generally, any index schedule satisfying (8) has a convergent physical frequency. Hence an argument that diagonalizes the Huxley–Watt annulus in the finite log interval and then attempts to bound one such mode separately at the square-scale target is not an intermediate theorem: it is already an RH-equivalent obligation.

This includes a much larger family than fixed `k`. For example:

- `k_N` bounded or `k_N=o(log N)` gives `\tau_N->0`;
- `k_N=floor(\kappa log N)` gives `\tau_N->2\pi\kappa`;
- any perturbation `k_N=\kappa log N+o(log N)` has the same limiting character.

The conclusion is scalar. It does not prohibit cancellation among several such modes when their signed combination is retained before taking absolute values. Indeed, `MC-035`–`MC-036` already identify coupled cancellation as the main surviving possibility.

## 5. Prior art and novelty assessment

The RH-equivalent bound

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\]

is classical Littlewood–Titchmarsh theory and is represented in `research/prior_art/mobius-summatory-criterion.md`. `MC-036` already records E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Clarendon Press / Oxford University Press (1986), §14.25, as a standard monograph anchor. Abel/partial summation for fixed complex power weights is also standard Dirichlet-polynomial technology.

The Huxley–Watt annular coefficient and its exact Mellin factorization are not new here; they are inherited from `MC-032`–`MC-036` and ultimately from the Huxley–Watt finite-cutoff framework recorded as `MC-S24`.

A targeted literature search for endpoint-dependent or slowly varying Mellin twists of the Mertens sum did not identify a standard named criterion that should be claimed as new prior art for (2). Absence from such a search is not evidence of novelty, and none is claimed. The durable contribution is the **line-specific information audit**: a simple self-absorption argument shows that convergence of the scale-dependent character is enough to recover the fixed-character RH burden, closing a concrete escape explicitly left open by `MC-036`.

## 6. Boundaries and decisive continuation

This finding does **not** prove that every `N`-dependent Mellin schedule is RH-equivalent. The argument uses `\tau_N-\tau_* -> 0` so that the Volterra-type error in (13) can be absorbed. A bounded but persistently nonconvergent schedule, an unbounded/high-frequency schedule, or a mode family whose physical frequency oscillates between separated values is not covered by this theorem.

It also does not give a lower bound for the full Huxley–Watt sawtooth functional. Different annular characters can cancel one another, and a source-natural coupled estimate may exploit information destroyed by modewise absolute values.

The decisive next test for the accepted reciprocal-phase / prime-log-slab direction is therefore no longer a fixed-index or asymptotically fixed-frequency scalar estimate. A viable harmonic continuation must exhibit one of the following with an independently weaker proof obligation:

1. a genuinely coupled signed estimate across log frequencies;
2. a nonconvergent or high-frequency scale law whose control cannot be reduced by the present self-absorption argument to one fixed character;
3. an arithmetic mechanism that forces the coarse/fixed-frequency components from other controlled information rather than estimating those components directly.

A proposal whose physical Mellin frequency converges and whose decisive step is a separate `N^{1+o(1)}` annular mode bound has simply relocated the complete RH burden.

## Consequence for the research line

`MC-035` found an RH-equivalent log-radial zero mode. `MC-036` extended the obstruction to every fixed Mellin frequency but left varying finite-interval modes formally open. `MC-038` now closes that escape for the entire class of **convergent physical frequency schedules**.

The harmonic frontier is correspondingly more specific. The current Huxley–Watt annular route can survive only through coupled mode cancellation, genuinely nonconvergent/high-frequency behavior, or a new arithmetic production law. Scalarization along any asymptotically fixed Mellin character is already RH-complete.