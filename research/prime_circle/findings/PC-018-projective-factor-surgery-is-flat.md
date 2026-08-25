# PC-018 — factor-introduction surgery has zero projective curvature

**Status:** `DECISIVE-NEGATIVE` for a hoped-for noncommutative/holonomy mechanism based on the order of introducing prime factors.

PC-017 suggested a possible new direction: multiplication by a prime already dividing the level gives an exact cyclic cover, while introducing a new prime factor requires cover + uniformization surgery. A natural out-of-the-box question is therefore whether introducing two new primes in different orders produces a nontrivial projective holonomy or curvature.

The answer is no at the canonical Fuchsian projective-connection level. The square is exactly flat.

## 1. Canonical pullback operator

For the primitive-shell surface

\[
S_n=\widehat{\mathbb C}\setminus\bigl(\{0,\infty\}\cup\mu_n^*\bigr),
\]

let \(Q_n\) denote its Fuchsian projective connection.

For an integer \(r\ge2\), define the projective pullback under \(F_r(z)=z^r\) by

\[
\mathscr P_r Q(z)
:=r^2z^{2r-2}Q(z^r)-\frac{r^2-1}{2z^2}.
\]

The second term is the Schwarzian

\[
\{z^r,z\}=-\frac{r^2-1}{2z^2}.
\]

The Schwarzian chain rule implies the exact semigroup law

\[
\boxed{\mathscr P_q\mathscr P_p=\mathscr P_{pq}.}
\]

For a quadratic differential \(A(z)dz^2\), the corresponding linear pullback is

\[
\mathscr L_r A(z):=r^2z^{2r-2}A(z^r).
\]

The difference of two projective pullbacks satisfies

\[
\boxed{
\mathscr P_r Q_1-\mathscr P_r Q_2
=\mathscr L_r(Q_1-Q_2).
}
\]

## 2. One-step surgery defect

Define the canonical projective defect of the multiplicative step \(n\to nr\) by

\[
\boxed{
\mathcal A_{n,r}
:=Q_{nr}-\mathscr P_r Q_n.
}
\]

It is understood meromorphically on the common domain; when \(r\mid n\), PC-016/017 give an honest cyclic cover and

\[
\boxed{\mathcal A_{n,r}=0.}
\]

When \(r\nmid n\), \(\mathcal A_{n,r}\) is the projective/accessory-parameter defect caused by filling the inherited-shell cusps after taking the complete preimage.

## 3. Exact cocycle identity

For any positive integers \(p,q\ge2\),

\[
\begin{aligned}
\mathcal A_{n,pq}
&=Q_{npq}-\mathscr P_{pq}Q_n\\
&=Q_{npq}-\mathscr P_qQ_{np}
+\mathscr P_qQ_{np}-\mathscr P_q\mathscr P_pQ_n\\
&=\mathcal A_{np,q}+\mathscr L_q\mathcal A_{n,p}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal A_{n,pq}
=\mathcal A_{np,q}+\mathscr L_q\mathcal A_{n,p}.
}
\]

Repeating the same computation in the opposite order gives

\[
\boxed{
\mathcal A_{n,pq}
=\mathcal A_{nq,p}+\mathscr L_p\mathcal A_{n,q}.
}
\]

Therefore the discrete multiplicative square has identically zero curvature:

\[
\boxed{
\mathcal F_{n;p,q}
:=
\mathcal A_{np,q}+\mathscr L_q\mathcal A_{n,p}
-\mathcal A_{nq,p}-\mathscr L_p\mathcal A_{n,q}
=0.
}
\]

This holds regardless of whether \(p,q\) are old or new prime factors. In particular it kills the hoped-for mechanism

\[
\text{introduce }p\text{ then }q
\quad\text{vs}\quad
\text{introduce }q\text{ then }p
\longrightarrow
\text{nontrivial projective holonomy}.
\]

There is no such holonomy: the canonical projective defect is an exact 1-cocycle.

## 4. Why the result is structural, not accidental

The Schwarzian derivative is the classical projective 1-cocycle:

\[
\{f\circ g,z\}
=(g')^2\{f,g(z)\}+\{g,z\}.
\]

Projective connections form an affine space over quadratic differentials, and their pullbacks inherit precisely this cocycle structure. Thus any construction that accumulates only differences of canonical projective connections along multiplicative power maps is path-independent once endpoints are fixed.

This is standard projective-connection/Schwarzian theory. The prime-circle-specific content of the present finding is the negative application to the proposed "prime-factor creation curvature" suggested by PC-017.

## 5. Metric version is flat as well

The same obstruction appears before taking the holomorphic stress tensor. Let \(g_n\) be the complete Poincare metric of \(S_n\), and compare \(g_{nr}\) with the pullback \(F_r^*g_n\) on their common punctured domain. The logarithmic conformal defect

\[
\delta_{n,r}
:=\log\frac{\rho_{F_r^*g_n}}{\rho_{g_{nr}}}
\]

adds under successive pullbacks because conformal factors multiply. On a common domain,

\[
\boxed{
\delta_{n,pq}
=\delta_{np,q}+\delta_{n,p}\circ F_q
=\delta_{nq,p}+\delta_{n,q}\circ F_p.
}
\]

So an order-sensitive curvature does not reappear at the scalar Liouville-metric level.

## 6. What this rules out

It is not useful to pursue a mechanism in which RH information is supposed to live in a noncommutativity/holonomy generated solely by the order of prime-factor introduction under the canonical maps \(z\mapsto z^p\). At both the metric-defect and projective-connection levels, the multiplicative category is flat in exactly the relevant sense.

Likewise, iterated additive accumulation of \(\mathcal A_{n,p}\) along a factorization path cannot contain information about the ordering of factors that is absent from the endpoints; the cocycle telescopes to the single endpoint defect.

This does **not** trivialize the endpoint accessory parameters themselves. A nonzero mixed interaction may still arise from nonlinear functionals of the endpoint uniformization, e.g. the Hessian of the Liouville action / Weil-Petersson geometry, determinants, or monodromy representations. What is ruled out is the simpler "curvature of factor-order" branch.

## 7. Novelty check

The mathematical mechanism is classical:

- the Schwarzian chain rule is the one-dimensional projective 1-cocycle;
- differences of projective connections are quadratic differentials;
- analogous projective-connection cocycles are standard in the literature (e.g. Bouarroudj--Ovsienko);
- Fuchsian uniformizing connections and accessory parameters on punctured spheres are classical (Kra, Takhtajan--Zograf).

No novelty is claimed for the cocycle identity itself. The substantive result here is a decisive falsification of a specific new branch opened by the prime-circle birth-shell construction.

## Research consequence

Do not seek arithmetic information in path-order holonomy of the cover/surgery steps. The remaining genuinely nonlinear sector must be an endpoint or second-variation object: accessory/monodromy data after forced poles are removed, Liouville-action interactions, Weil-Petersson geometry, or another invariant that is not an exact first-difference cocycle.
