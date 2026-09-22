# AF-510 — Curvature has an explicit canonical inverse on the dilation quotient

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `RECOVERY-MAP` · `DIRICHLET-SOURCE` · `QUOTIENT-INVERSE` · `TAIL-ASYMPTOTIC` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
Q=\{q_1<q_2<\cdots\},\qquad 1<q_1,\qquad q_n\to\infty,
\]

be a simple unit-weight positive source for which

\[
P_Q(s)=\sum_{n\ge1}q_n^{-s}
\]

converges absolutely on `s>\sigma_0`. Write

\[
\kappa_Q(s)=\frac{d^2}{ds^2}\log P_Q(s)
\]

and normalize the source by its smallest atom,

\[
\lambda_n:=\log\frac{q_n}{q_1},
\qquad
0=\lambda_1<\lambda_2<\cdots .
\]

AF-509 classifies the fibers of `Q\mapsto\kappa_Q`: two simple unit-weight sources have the same curvature profile exactly when they differ by a common dilation. The quotient inverse can in fact be written explicitly. Define

\[
H_Q(s):=\int_s^\infty (t-s)\,\kappa_Q(t)\,dt .
\tag{1}
\]

Then the integral converges and

\[
\boxed{
H_Q(s)=\log\!\left(q_1^sP_Q(s)\right)
       =\log\!\left(1+\sum_{n\ge2}e^{-s\lambda_n}\right).
}
\tag{2}
\]

Consequently

\[
\boxed{
F_Q(s):=e^{H_Q(s)}-1
       =\sum_{n\ge2}e^{-s\lambda_n}.
}
\tag{3}
\]

Thus the curvature profile itself recovers the complete normalized ratio source

\[
\left\{\frac{q_n}{q_1}:n\ge1\right\}
\]

without choosing an integration constant, a base point, or an external scale. The only information absent from `\kappa_Q` is the global dilation already identified in AF-509.

There is also a direct tail carrier for the first nontrivial normalized ratio. With

\[
\delta:=\lambda_2=\log\frac{q_2}{q_1},
\]

one has

\[
\boxed{
\kappa_Q(s)=\delta^2e^{-\delta s}(1+o(1))
\qquad(s\to\infty),
}
\tag{4}
\]

and therefore

\[
\boxed{
\delta=-\lim_{s\to\infty}\frac{1}{s}\log \kappa_Q(s),
\qquad
\frac{q_2}{q_1}=e^\delta .
}
\tag{5}
\]

More generally, after forming `F_Q` in `(3)`, the whole normalized source can be peeled recursively:

\[
\lambda_2=-\lim_{s\to\infty}\frac1s\log F_Q(s),
\tag{6}
\]

and, once `\lambda_2,\ldots,\lambda_{m-1}` are known,

\[
F_{Q,m}(s):=
F_Q(s)-\sum_{j=2}^{m-1}e^{-s\lambda_j}
=\sum_{j\ge m}e^{-s\lambda_j}
\]

satisfies

\[
\boxed{
\lambda_m=-\lim_{s\to\infty}\frac1s\log F_{Q,m}(s).
}
\tag{7}
\]

Equations `(1)`--`(7)` give a canonical constructive inverse of the curvature compression on the dilation quotient. They also expose the conditioning boundary: exact recovery is complete, but deeper atoms are represented by exponentially smaller residuals after successive peeling, so exact fidelity does not imply stable finite-precision recovery.

## Derivation

### 1. Fix the dilation gauge canonically

Put

\[
Z_Q(s):=q_1^sP_Q(s)
       =\sum_{n\ge1}\left(\frac{q_1}{q_n}\right)^s
       =1+\sum_{n\ge2}e^{-s\lambda_n}.
\tag{8}
\]

Because multiplication of `P_Q` by `q_1^s` adds the affine term `s\log q_1` to its logarithm,

\[
\frac{d^2}{ds^2}\log Z_Q(s)=\kappa_Q(s).
\tag{9}
\]

Absolute convergence of `P_Q` on a half-line implies absolute convergence of the normalized exponential sum there. Since `\lambda_2>0`,

\[
Z_Q(s)\to1,
\qquad
\log Z_Q(s)\to0
\qquad(s\to\infty).
\tag{10}
\]

Termwise differentiation on every slightly smaller right half-line gives

\[
(\log Z_Q)'(s)\to0.
\tag{11}
\]

These two boundary conditions are the canonical conditions associated with the quotient representative whose smallest normalized atom is `1`.

### 2. Two integrations recover the normalized log-Laplace transform

Let

\[
h(s):=\log Z_Q(s).
\]

From `(9)`, `h''=\kappa_Q`. Integrating from `s` to infinity and using `(11)`,

\[
h'(s)=-\int_s^\infty \kappa_Q(t)\,dt.
\tag{12}
\]

Integrating once more and using `(10)`, Tonelli/Fubini for the nonnegative curvature gives

\[
\begin{aligned}
h(s)
&=\int_s^\infty\int_u^\infty \kappa_Q(t)\,dt\,du\\
&=\int_s^\infty (t-s)\kappa_Q(t)\,dt.
\end{aligned}
\tag{13}
\]

This proves `(1)`--`(2)`. Exponentiating `(2)` and subtracting the normalized leading atom gives `(3)`.

The important point is that the two affine constants normally created by integrating a second derivative do not reappear as arbitrary choices. On the quotient section `q_1=1`, positivity and the simple unit leading atom force the boundary conditions `h(\infty)=h'(\infty)=0`. The quotient geometry therefore supplies the missing integration data intrinsically.

### 3. Positive exponential peeling recovers every normalized atom

Equation `(3)` is a positive discrete Laplace sum with strictly increasing exponents. For any fixed `m\ge2`, suppose `\lambda_2,\ldots,\lambda_{m-1}` have already been recovered. Then

\[
F_{Q,m}(s)
=e^{-s\lambda_m}
\left(
1+\sum_{j>m}e^{-s(\lambda_j-\lambda_m)}
\right).
\tag{14}
\]

Choose a real `s_0` in the convergence half-line. Since `\lambda_{m+1}>\lambda_m`, for `s\ge s_0` the remaining tail is bounded by

\[
\sum_{j>m}e^{-s(\lambda_j-\lambda_m)}
\le
C_m e^{-(s-s_0)(\lambda_{m+1}-\lambda_m)}
\tag{15}
\]

for a finite `C_m` obtained from the convergent sum at `s_0`. Hence the parenthesis in `(14)` tends to `1`, so

\[
-\frac1s\log F_{Q,m}(s)\to\lambda_m.
\]

This proves `(6)`--`(7)` and gives an elementary constructive version of the usual uniqueness of positive discrete Laplace/generalized Dirichlet sums.

### 4. The curvature tail already exposes the first normalized gap

Let `\delta=\lambda_2`. Write

\[
Z_Q(s)=1+e^{-\delta s}+R(s),
\qquad
R(s)=O(e^{-\lambda_3 s})
\tag{16}
\]

when a third atom is present; the same argument is simpler for a two-atom finite source. The bound follows from absolute convergence at a fixed right-half-line point exactly as in `(15)`. Differentiated versions of the remainder have the same strictly faster exponential rate after moving the fixed convergence point slightly to the right.

Since

\[
\log(1+u)=u+O(u^2)
\qquad(u\to0),
\]

with `u=e^{-\delta s}+R(s)`, one obtains

\[
\log Z_Q(s)
=e^{-\delta s}+o(e^{-\delta s}).
\tag{17}
\]

Differentiating twice within the absolute-convergence half-line gives

\[
\kappa_Q(s)
=(\log Z_Q)''(s)
=\delta^2e^{-\delta s}+o(e^{-\delta s}),
\tag{18}
\]

which is `(4)`. Taking logarithms yields `(5)`.

For the rational primes,

\[
q_1=2,\qquad q_2=3,
\]

so the prime-curvature tail has the exact leading scale-free fingerprint

\[
\boxed{
\kappa_{\mathbb P}(s)
\sim
\left(\log\frac32\right)^2\left(\frac23\right)^s.
}
\tag{19}
\]

This does not by itself distinguish `\mathbb P` from a common dilation `c\mathbb P`; that collision is the exact quotient fiber of AF-509.

## Fidelity and control audit

The recovery is not ordinary injectivity in disguise. The map `Q\mapsto\kappa_Q` is genuinely noninjective on unrestricted simple sources because every common dilation satisfies

\[
\kappa_{cQ}=\kappa_Q.
\]

What `(1)`--`(7)` show is stronger and more structured: after passing to the intended dilation quotient, the compression has a canonical section and an explicit inverse.

The matched controls are therefore exact and exhausted by the AF-509 fiber classification. `Q` and `cQ` remain indistinguishable from curvature alone, while their normalized ratio sources coincide exactly. No extra labeling or hidden copy of `Q` has been inserted into the inverse: `(1)` uses only the observed curvature profile, and the boundary normalization is forced by choosing the intrinsic quotient representative with smallest atom `1`.

The arithmetic category restriction from AF-509 remains separate information. Primitive integer support can pin the global scale and turn the quotient-faithful curvature profile into full source fidelity, but neither `(1)` nor the tail asymptotics derive integrality. In particular, the explicit inverse does not eliminate nonintegral dilated Beurling controls; it identifies precisely what they share.

## Prior art and novelty assessment

No novelty is claimed for the analytic ingredients.

- The identity between the Hessian/second derivative of a cumulant transform and variance under exponential tilting is standard natural-exponential-family theory. The *Encyclopedia of Mathematics* article **“Natural exponential family of probability distributions”** records the cumulant-Hessian/variance relation and the classical determination of a natural exponential family from its variance structure.
- David V. Widder, ***The Laplace Transform***, Princeton University Press (1941), is a classical source for Laplace-transform representation and uniqueness.
- G. H. Hardy and Marcel Riesz, ***The General Theory of Dirichlet's Series***, Cambridge Tracts in Mathematics and Mathematical Physics 18 (1915), is classical background for generalized Dirichlet sums and their uniqueness.
- AF-509 already establishes the exact dilation fiber classification for this curvature compression. The present result does not replace that theorem; it supplies the canonical recovery map and the exact tail carrier inside the quotient that the fiber classification leaves implicit.

The durable Arithmetic Fidelity delta is therefore organizational and constructive rather than a claim of a new Laplace-transform theorem: **the quotient is not only identifiable, it has an intrinsic inverse obtained by double tail integration, and the first normalized generator ratio is already visible as the exponential decay rate of the curvature itself.**

## Boundaries and failure modes

- **Exact profile, not finite samples.** Formula `(1)` requires the exact tail profile. Equality on an open interval determines the analytic profile abstractly, but analytic continuation from finite/noisy data is a different and generally unstable problem.
- **Unit leading mass is load bearing.** The boundary value `Z_Q(\infty)=1` uses the simple unit-weight first atom. For a general positive weighted source, curvature still forgets an overall mass factor as well as support translation; an additional normalization is required.
- **Peeling is not a stability theorem.** The residual `F_{Q,m}` becomes exponentially small as `m` increases or as the observation point moves right. Equations `(6)`--`(7)` are exact-identification formulas, not guarantees of useful recovery under noise.
- **The normalized source is the quotient object.** Recovering all ratios `q_n/q_1` is complete only modulo global dilation. Any application needing the absolute rational-prime norms still requires an independently justified scale anchor or source-class restriction.
- **No finite-precision prime discriminator is established.** Equation `(19)` is an exact asymptotic fingerprint of the first normalized prime ratio, but many non-prime systems can share finitely many initial ratios or approximate the tail over finite windows. Prime provenance still requires a control class and a quantitative observation model.

## Consequences for the research line

AF-509 showed that log-prime-sum curvature loses exactly one gauge degree of freedom. AF-510 makes that statement operational at the exact level: the curvature can be integrated with canonical boundary conditions to recover the normalized positive Laplace sum, after which the normalized generators are recovered one by one.

This separates two questions that should not be conflated in later prime applications. **Exact structural fidelity modulo dilation is solved for this compression. Quantitative fidelity is not.** The next meaningful question is therefore not whether the curvature contains the normalized source in principle, but how much of that inverse survives a declared finite window, sampling scheme, and noise/correlation law, and whether an arithmetic source restriction supplies the missing absolute scale without smuggling in the desired discriminator.