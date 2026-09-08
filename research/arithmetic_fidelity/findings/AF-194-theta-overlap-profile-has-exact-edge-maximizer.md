# AF-194 — Theta overlap profile has an exact edge maximizer

**Status:** `EXACT-DERIVED`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `LITERATURE-CONTEXT`, `NO-NOVELTY-CLAIM`

## Claim

AF-190 expresses the finite-overlap Euler-band discrepancy through the profile

\[
\Phi_{a,\tau}(u)
=
\sum_{n\in\mathbb Z}
\exp\!\left[
-an-
\frac{\pi^2\tau}{8}(n-u)^2
\right],
\qquad 0\le u\le1,
\tag{1}
\]

and the constant

\[
M(a,\tau)=\sup_{0\le u\le1}\Phi_{a,\tau}(u),
\qquad a>0,\ \tau>0.
\tag{2}
\]

The supremum is in fact unnecessary. For every `a>0` and `tau>0`,

\[
\boxed{
\Phi_{a,\tau}(u)<\Phi_{a,\tau}(0)
\quad\text{for every }0<u\le1,
}
\tag{3}
\]

so

\[
\boxed{
M(a,\tau)=\Phi_{a,\tau}(0)
=1+2\sum_{n\ge1}
\cosh(an)
\exp\!\left(-\frac{\pi^2\tau}{8}n^2\right).
}
\tag{4}
\]

Thus the finite-overlap profile is always optimized at the first reachable reciprocal edge `u=0`; there is no interior optimizer transition as `tau` varies. The interior oscillation of the tilted theta function can create local extrema, but none can exceed the edge value.

Combined with AF-190, this sharpens its asymptotic to

\[
\boxed{
D_\delta
=(2+o(1))
\frac{e^{-a q_\delta}}{q_\delta}
\left[
1+2\sum_{n\ge1}
\cosh(an)e^{-\pi^2\tau n^2/8}
\right]
}
\tag{5}
\]

whenever

\[
q_\delta\to\infty,
\qquad
\frac{m_\delta}{q_\delta^2}\to\tau\in(0,\infty),
\qquad
m_\delta q_\delta\delta\to0.
\tag{6}
\]

The `u=0` statement is about the macroscopic reciprocal-resonance coordinate used in AF-190. Its phase-alignment argument may still move the actual observing frequency by `O(1)` in `t`, equivalently `O(delta)` in `theta=t delta`, to align the contributing harmonics. No claim is made that the literal band-edge frequency itself always realizes the full complex-valued asymptotic constant without that microscopic adjustment.

## Reduction to a tilted discrete Gaussian

Put

\[
c=\frac{\pi^2\tau}{8}>0,
\qquad
b=\frac{a}{2c}>0.
\tag{7}
\]

Define the Gaussian lattice mass

\[
Z_b=\sum_{n\in\mathbb Z}e^{-c(n+b)^2}
\tag{8}
\]

and the probability law

\[
\mathbb P_b(N=n)=\frac{e^{-c(n+b)^2}}{Z_b}.
\tag{9}
\]

Completing the square in `(1)` gives

\[
\Phi_{a,\tau}(u)
=e^{cb^2-2cbu}Z_{b-u}.
\tag{10}
\]

For `0\le u\le1`,

\[
Z_{b-u}
=
Z_b\,
 e^{2cbu-cu^2}
\mathbb E_b e^{2cuN},
\tag{11}
\]

hence the special relation `a=2cb` cancels the external tilt exactly:

\[
\boxed{
\frac{\Phi_{a,\tau}(u)}{\Phi_{a,\tau}(0)}
=
e^{-cu^2}\mathbb E_b e^{2cuN}.
}
\tag{12}
\]

The maximization problem is therefore an exponential-moment comparison for a one-dimensional shifted discrete Gaussian.

## Negative tilting can only reduce positive exponential moments

Let `P_0` denote the centered discrete Gaussian

\[
\mathbb P_0(N=n)
=
\frac{e^{-cn^2}}{Z_0}.
\tag{13}
\]

The shifted law `(9)` is its negative exponential tilt:

\[
\mathbb P_b(N=n)
=
\frac{
\mathbb P_0(N=n)e^{-2cbn}
}{
\mathbb E_0e^{-2cbN}
}.
\tag{14}
\]

For `u\ge0`, the function `f(n)=e^{2cun}` is increasing in `n`, while `g(n)=e^{-2cbn}` is decreasing. Their covariance under any probability law on the ordered set `Z` is nonpositive. Explicitly, for independent `N,N'` with law `P_0`,

\[
2\operatorname{Cov}_0(f(N),g(N))
=
\mathbb E
\left[(f(N)-f(N'))(g(N)-g(N'))\right]
\le0.
\tag{15}
\]

Therefore

\[
\mathbb E_0[f(N)g(N)]
\le
\mathbb E_0f(N)\,\mathbb E_0g(N),
\tag{16}
\]

and `(14)` yields

\[
\boxed{
\mathbb E_b e^{2cuN}
\le
\mathbb E_0 e^{2cuN}.
}
\tag{17}
\]

This is the elementary monotone-likelihood-ratio step: shifting the Gaussian center to the left cannot increase an increasing exponential moment.

## The centered lattice Gaussian has the continuous Gaussian MGF as an envelope

Let

\[
G(u)=\sum_{n\in\mathbb Z}e^{-c(n-u)^2}.
\tag{18}
\]

Completing the square gives

\[
\mathbb E_0e^{2cuN}
=
e^{cu^2}\frac{G(u)}{G(0)}.
\tag{19}
\]

Poisson summation gives the classical theta expansion

\[
G(u)
=
\sqrt{\frac\pi c}
\sum_{k\in\mathbb Z}
 e^{-\pi^2k^2/c}e^{2\pi iku}
\tag{20}
\]

and therefore

\[
G(u)
=
\sqrt{\frac\pi c}
\left[
1+2\sum_{k\ge1}
 e^{-\pi^2k^2/c}\cos(2\pi ku)
\right]
\le G(0).
\tag{21}
\]

For `0<u<1`, the inequality is strict because already the `k=1` cosine is strictly smaller than one and every Fourier coefficient in `(21)` is positive. Hence

\[
\boxed{
\mathbb E_0e^{2cuN}
\le e^{cu^2},
}
\tag{22}
\]

with strict inequality for `0<u<1`.

Combining `(12)`, `(17)`, and `(22)` proves

\[
\Phi_{a,\tau}(u)
\le\Phi_{a,\tau}(0),
\tag{23}
\]

strictly for `0<u<1`. At the other endpoint AF-190's exact quasi-periodicity gives

\[
\Phi_{a,\tau}(1)=e^{-a}\Phi_{a,\tau}(0)<\Phi_{a,\tau}(0),
\tag{24}
\]

which completes `(3)`.

## Exact primal and dual theta representations

Pairing the `n` and `-n` terms of `(4)` gives the rapidly convergent large-`tau` representation

\[
\boxed{
M(a,\tau)
=
1+2\sum_{n\ge1}
\cosh(an)e^{-\pi^2\tau n^2/8}.
}
\tag{25}
\]

In particular, for fixed `a>0`,

\[
\boxed{
M(a,\tau)
=
1+2\cosh(a)e^{-\pi^2\tau/8}
+O_a\!\left(e^{-\pi^2\tau/2}\right)
\qquad(\tau\to\infty).
}
\tag{26}
\]

Thus AF-189's isolated-resonance constant `1` is approached at an explicitly exponential rate at the level of the finite-overlap theta profile.

Applying Poisson summation after completing the square instead gives the exact modular representation

\[
\boxed{
M(a,\tau)
=
\sqrt{\frac{8}{\pi\tau}}
\exp\!\left(\frac{2a^2}{\pi^2\tau}\right)
\left[
1+2\sum_{k\ge1}
 e^{-8k^2/\tau}
\cos\!\left(\frac{8ak}{\pi\tau}\right)
\right].
}
\tag{27}
\]

Equation `(27)` recovers the small-`tau` modular asymptotic used in AF-193, now without a separate optimizer question:

\[
M(a,\tau)
=
\sqrt{\frac{8}{\pi\tau}}
\exp\!\left(\frac{2a^2}{\pi^2\tau}\right)
\left(1+O(e^{-8/\tau})\right).
\tag{28}
\]

The two exact series `(25)` and `(27)` expose the same fidelity constant in the regimes where the original theta lattice or its Poisson dual is sparse.

## What this changes in the Euler fidelity picture

AF-190 left `M(a,tau)` as a variational constant over the reciprocal offset `u`. AF-193 showed that `u=0` is optimal in the small-`tau` regime relevant to theta-to-saddle matching. The present argument removes that restriction: **the first reachable reciprocal edge is the global profile maximizer for every finite overlap parameter `tau>0`.**

This rules out an additional source-complexity transition that could otherwise have appeared through migration of the theta-profile optimizer. The genuine transitions identified by AF-189--AF-193 therefore come from resonance overlap and saddle scaling, not from a change in the maximizing reciprocal offset.

The proof also illustrates a useful fidelity pattern independent of the Euler specialization. A tilted lattice response can sometimes be controlled by separating two effects: monotone likelihood-ratio ordering handles the source tilt, while a positive-coefficient Poisson/theta expansion supplies the centered sub-Gaussian envelope. In this case those two classical mechanisms collapse a nontrivial-looking variational profile to one canonical boundary value.

## Prior art and novelty assessment

The ingredients are classical and no novelty claim is made for the underlying theta or discrete-Gaussian inequalities.

- NIST Digital Library of Mathematical Functions, Chapter 20, especially §20.2 and §20.7(viii), records the Jacobi theta Fourier series, quasi-periodicity, and modular transformations underlying `(20)` and `(27)`.
- Oded Regev and Noah Stephens-Davidowitz, **“An Inequality for Gaussians on Lattices,”** *SIAM Journal on Discrete Mathematics* 31(2) (2017), 749–757, DOI `10.1137/15M1052226`, develops Gaussian-mass inequalities on lattice cosets and derives moment and heat-kernel monotonicity consequences. It is direct prior-art context for treating theta masses and discrete-Gaussian moments through lattice Gaussian inequalities.
- Daniele Agostini and Carlos Améndola, **“Discrete Gaussian Distributions via Theta Functions,”** *SIAM Journal on Applied Algebra and Geometry* 3(1) (2019), 1–30, DOI `10.1137/18M1164937`, is direct modern prior art for the theta-function parametrization and statistical properties of discrete Gaussian laws.

The monotone-tilt comparison `(14)`--`(17)` and the centered bound `(19)`--`(22)` are derived directly here from elementary covariance ordering and Poisson summation. A targeted search did not identify a source stating the exact AF-190 profile identity `(4)` in this notation or its Euler-band consequence `(5)`. That absence is not evidence of priority. The durable contribution is the exact closure of AF-190's optimizer and the removal of a possible spurious phase boundary from the local Arithmetic Fidelity picture.

## Boundaries and falsification

- The maximizer theorem concerns exactly the exponentially tilted Gaussian-lattice profile `(1)`. Changing the harmonic coefficient bias away from `e^{-an}` can invalidate the monotone-likelihood-ratio reduction.
- The proof uses `a>0`. At `a=0`, both endpoints agree by periodicity and the strict uniqueness statement changes, although `u=0` remains a maximizer.
- Equation `(5)` inherits every hypothesis and boundary of AF-190: the AF-182 parity-split controls, Euler local logarithm, continuous observation band, and `m q delta -> 0` damping regime.
- The profile theorem does not make the parity controls extremal among all positive source pairs and does not provide a minimax inverse-recovery theorem.
- The large-`tau` expansion `(26)` is an asymptotic of the profile `M(a,tau)`. Passing it directly into a triangular array with `tau=tau_delta->infinity` requires the uniformity hypotheses supplied by AF-189/AF-192 rather than the fixed-`tau` limit statement of AF-190.
- No rational-prime specificity or RH consequence follows from the result.

## Dependencies and evidence boundary

The finding uses AF-190 for the Euler-band reduction to `M(a,tau)` and AF-193 only for comparison with the previously derived small-`tau` matching regime. The proof of `(3)`--`(4)` is otherwise independent of their saddle analysis.

No numerical experiment is used as evidence. Numerical exploration was not needed for the proof. The exact theorem is the lattice-Gaussian inequality `(3)` and its consequence that AF-190's variational constant is the explicit boundary series `(4)`.