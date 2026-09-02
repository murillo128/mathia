# MC-019 — The Mertens path-energy scale already contains an RH-equivalent coarse Riesz mode

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
M(x)=\sum_{n\le x}\mu(n),
\qquad
V_M(N)=\sum_{k=0}^{N-1}|M(k)|^2
\]

with `M(0)=0`, so this `V_M` is exactly the path-energy carrier used in `MC-016` and `MC-017`. Define the first-order Möbius Riesz sum

\[
R_1(x)=\sum_{n\le x}(x-n)\mu(n)
      =\int_1^x M(u)\,du.
\tag{1}
\]

For integer `N`, finite summation gives

\[
R_1(N)=\sum_{k=0}^{N-1}M(k).
\tag{2}
\]

Then the following three assertions are equivalent:

1. the Riemann hypothesis;
2. for every `epsilon>0`,
   \[
   R_1(x)=O_\varepsilon\!\left(x^{3/2+\varepsilon}\right);
   \tag{3}
   \]
3. for every `epsilon>0`,
   \[
   V_M(N)=O_\varepsilon\!\left(N^{2+\varepsilon}\right).
   \tag{4}
   \]

Thus the RH-scale path-energy target from `MC-016`/`MC-017` is not intrinsically a weaker endpoint than RH. Its constant/coarse projection already carries an RH-equivalent first Riesz mean.

More precisely, for the prefix vector

\[
m_N=(M(0),M(1),\ldots,M(N-1))\in\mathbb C^N
\]

and the normalized constant vector

\[
u_N=N^{-1/2}(1,\ldots,1),
\]

one has

\[
\langle m_N,u_N\rangle=\frac{R_1(N)}{\sqrt N},
\qquad
\frac{|R_1(N)|^2}{N}\le V_M(N).
\tag{5}
\]

Equation (5) is exactly the energy of the constant mode in any orthogonal decomposition that separates constants. In Haar language it is the top scaling coefficient. Therefore the `MC-018` escape route “retain an explicit coarse/scaling coefficient together with local details” is mathematically real but does **not** lower the difficulty merely by changing coordinates: controlling that coefficient at the scale forced by (4) already gives an RH-equivalent Riesz bound.

The surviving multiscale question is narrower. A useful decomposition must derive the coarse coefficient from independently weaker arithmetic input, couple it nonlinearly to detail information, or otherwise explain why the required Riesz bound follows without assuming an equivalent global cancellation statement.

## 1. The coarse coefficient is the first Riesz sum

For integer `N`, reverse the finite sums:

\[
\begin{aligned}
\sum_{k=0}^{N-1}M(k)
&=\sum_{k=0}^{N-1}\sum_{n\le k}\mu(n)\\
&=\sum_{n=1}^{N-1}(N-n)\mu(n)\\
&=R_1(N).
\end{aligned}
\tag{6}
\]

Taking the inner product with the normalized constant vector proves the first identity in (5). Cauchy–Schwarz gives

\[
|R_1(N)|^2
\le N\sum_{k=0}^{N-1}|M(k)|^2
=N V_M(N),
\tag{7}
\]

which proves the second identity in (5).

Consequently, if (4) holds for every positive epsilon, then for every positive epsilon, after applying (4) with `2 epsilon`,

\[
R_1(N)=O_\varepsilon(N^{3/2+\varepsilon}).
\tag{8}
\]

This extends from integer `N` to real `x`. If `N\le x<N+1`, then

\[
R_1(x)=R_1(N)+(x-N)M(N),
\tag{9}
\]

and `|M(N)|^2\le V_M(N+1)`. The interpolation term is therefore smaller than the `x^(3/2+epsilon)` target after another harmless epsilon relabeling.

No probability, zero formula, or mean-absolute Mertens theorem is used in this step.

## 2. The first Riesz scale analytically excludes zeros to the right of the critical line

For `Re(s)>1`, absolute convergence permits termwise integration in (1):

\[
\begin{aligned}
\int_1^\infty R_1(x)x^{-s-2}\,dx
&=\sum_{n\ge1}\mu(n)
  \int_n^\infty (x-n)x^{-s-2}\,dx\\
&=\frac{1}{s(s+1)}\sum_{n\ge1}\frac{\mu(n)}{n^s}\\
&=\frac{1}{s(s+1)\zeta(s)}.
\end{aligned}
\tag{10}
\]

The elementary kernel integral used here is

\[
\int_n^\infty (x-n)x^{-s-2}\,dx
=\frac{n^{-s}}{s(s+1)}.
\tag{11}
\]

Now assume (3). For every compact subset of `Re(s)>1/2`, choose `epsilon>0` smaller than its distance from the line `Re(s)=1/2`. Then

\[
R_1(x)x^{-s-2}
=O\!\left(x^{-\operatorname{Re}(s)-1/2+\varepsilon}\right),
\]

so the integral in (10) converges absolutely and locally uniformly there. It therefore defines a holomorphic function `F(s)` throughout `Re(s)>1/2`.

On `Re(s)>1`, equation (10) gives

\[
s(s+1)\zeta(s)F(s)=1.
\tag{12}
\]

On the connected domain `Re(s)>1/2`, `s\ne1`, both sides are holomorphic, so the identity theorem extends (12) throughout that domain. Hence `zeta(s)` cannot vanish anywhere with `Re(s)>1/2`. The functional equation and conjugation symmetry then exclude nontrivial zeros with `Re(s)<1/2`, proving RH.

Thus (3) implies RH without invoking the recent mean-absolute implication audited in `MC-009`--`MC-012`.

## 3. RH gives both the Riesz and path-energy scales

The classical Mertens criterion states that RH is equivalent to

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
\tag{13}
\]

Integrating (13) in (1) gives (3). Squaring (13) and summing gives, for any `delta>0`,

\[
V_M(N)
\ll_\delta \sum_{k<N}k^{1+2\delta}
\ll_\delta N^{2+2\delta}.
\tag{14}
\]

Taking `delta=epsilon/2` gives (4). Together with Sections 1--2 this closes the equivalence

\[
\mathrm{RH}
\Longleftrightarrow
R_1(x)=O_\varepsilon(x^{3/2+\varepsilon})
\Longleftrightarrow
V_M(N)=O_\varepsilon(N^{2+\varepsilon}).
\tag{15}
\]

The implication `V_M -> RH` is deliberately routed through the one-dimensional coarse projection `R_1`; it does not require control of every individual `M(N)`.

## 4. Prior art and novelty boundary

Riesz means of the Möbius function are established analytic-number-theory objects. Shōta Inoue, *Riesz mean of Möbius function*, RIMS Kôkyûroku 2203 (2021), 31--40, defines

\[
M_\tau(x)=\frac{1}{\Gamma(\tau+1)}
\sum_{n\le x}\mu(n)\left(1-\frac{n}{x}\right)^\tau
\]

and studies their relation to zeta zeros and zero multiplicity. For `tau=1`,

\[
xM_1(x)=R_1(x).
\tag{16}
\]

The source is available from Kyoto University's RIMS proceedings at
https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/2203-03.pdf ; its opening proposition also records the standard RH/Mertens equivalence (13).

Quan Yang, Jay Mehta and Shigeru Kanemitsu, *On Popov's explicit formula and the Davenport expansion*, Czechoslovak Mathematical Journal 73 (2023), 869--883, DOI `10.21136/CMJ.2023.0322-22`, likewise treats order-0 and order-1 Riesz sums for PNT-related arithmetic functions, explicitly including Möbius. This confirms that the order-1 Riesz object and its explicit-formula setting are prior art.

No novelty is claimed for Möbius Riesz means, Mellin transforms, the identity `1/zeta(s)=sum mu(n)n^{-s}` in its convergence half-plane, Cauchy–Schwarz, orthogonal projection onto constants, or multiresolution scaling coefficients. The line-specific contribution is the exact consequence for the active Mathia carrier: **the `N^(2+epsilon)` path-energy scale isolated in `MC-016`/`MC-017` already contains a one-dimensional RH-equivalent coarse mode**. This identifies precisely where a naive “local details plus one coarse coefficient” repair of `MC-018` can hide the full difficulty.

A targeted prior-art search found the established Riesz-mean literature above and adjacent explicit-formula treatments; it did not justify a novelty claim for (15), whose proof is elementary once the objects are aligned.

## 5. Boundaries and falsification consequences

This finding does **not** show that `V_M` is a useless target. An equivalent criterion can still be valuable if independently controlled arithmetic structure acts naturally on it. `MC-017` remains exact and its boundary-cancelled Fourier representation remains a faithful coordinate description of `V_M`.

It also does not rule out wavelets, frames, multiscale decompositions, nonlinear statistics, or local methods. The negative statement is narrower: a decomposition that simply stores the missing constant/coarse coefficient and then assumes it has RH-scale size has not reduced the problem. In a nonorthogonal frame the constant mode may be distributed among several coefficients rather than appearing as one scalar, but the Riesz functional (2) must still be reconstructible if the representation is complete.

Nor does (15) say that every sufficient estimate for `V_M` is circular. A theorem deriving (4) from genuinely weaker, independently proved arithmetic input would prove RH. The point is that `V_M` should no longer be described as a softer endpoint whose RH consequence depends on the still-audited Pintz mean-absolute theorem: it has a direct classical analytic route to RH through (10).

The decisive continuation of the active clue is therefore to attack the **production** of the coarse Riesz mode, not merely its representation. A proposed escape should do at least one of the following:

- derive `R_1(N)` at `N^(3/2+epsilon)` scale from source-natural arithmetic information that is demonstrably weaker than RH;
- prove a nonlinear or multiplicative coupling in which detail information forces the Riesz coarse coefficient without assuming it separately;
- construct a matched multiplicative exact-support comparator satisfying the proposed detail hypotheses while its Riesz coarse mode violates the required scale, thereby killing that transfer mechanism.

A purely linear coordinate change with an explicit top scaling coefficient is no longer a substantive escape from `MC-018`; it only relocates an RH-equivalent scalar obligation.

## Consequences for the active clue

The accepted mean-absolute transfer clue had narrowed to the coarse-mode reconstruction problem after `MC-017` and `MC-018`. Equation (15) sharpens that frontier in two ways.

First, the path-energy target now has an **independent exact RH implication**, so its strategic value no longer depends on accepting the recent Pintz mean-absolute zero-boundary theorem. Second, the most obvious multiscale escape from `MC-018` is classicalized: retaining a top constant/scaling coefficient is necessary for reconstruction, but at the required scale that coefficient is the first Möbius Riesz sum and already carries the whole RH zero-free obligation.

The unresolved question is consequently arithmetic rather than representational: what independently controlled Möbius mechanism, if any, can force that coarse Riesz mode from information that the existing local, averaged, and prime-harmonic controls do not already contain?