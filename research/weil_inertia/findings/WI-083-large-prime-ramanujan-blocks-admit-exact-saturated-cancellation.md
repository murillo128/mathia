# WI-083 — Large-prime Ramanujan blocks collapse to two moments and admit exact saturated cancellation

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It sharpens the doubly saturated scalar regime deliberately left open by WI-082.

For the signed finite-window Ramanujan operator

\[
A_\omega^{(N)}=\sum_m \omega_m B_m^{(N)},
\qquad
B_m^{(N)}=(c_m(i-j))_{0\le i,j<N},
\]

consider only prime moduli larger than the window. For every prime `p>N`, the finite section loses all information about `p` except the scalar coefficient of the identity:

\[
\boxed{B_p^{(N)}=pI_N-J_N,}
\]

where `J_N` is the all-ones matrix. Consequently every real signed combination supported on such primes has the exact two-parameter form

\[
\boxed{
A_\omega^{(N)}
=\left(\sum_p p\omega_p\right)I_N
-\left(\sum_p\omega_p\right)J_N.
}
\]

Its entire spectrum and inertia are therefore controlled by only the two scalar moments `sum p omega_p` and `sum omega_p`. In particular, for any three distinct primes

\[
N<p<q<r,
\]

the nonzero integer weights

\[
\boxed{
\omega_p=r-q>0,
\qquad
\omega_q=p-r<0,
\qquad
\omega_r=q-p>0
}
\]

give the exact matrix identity

\[
\boxed{
(r-q)B_p^{(N)}+(p-r)B_q^{(N)}+(q-p)B_r^{(N)}=0.
}
\]

This example already lies in WI-082's **doubly saturated** regime: both the positive and negative primitive-frequency dictionaries contain at least `N` modes. Hence the universal finite-window Ramanujan geometry itself permits complete signed cancellation once overcompleteness is reached. A generic metric, rank, inertia, pairwise-lcm, or finite-window argument that uses only the scalar Ramanujan blocks cannot force a residual sign in that regime. Any successful continuation must impose source-specific restrictions on the allowed moduli/weights or retain information discarded by scalarization.

## 1. Exact collapse for prime moduli larger than the window

For a prime `p`, the Ramanujan sum has the elementary values

\[
c_p(h)=
\begin{cases}
p-1,&p\mid h,\\
-1,&p\nmid h.
\end{cases}
\tag{1}
\]

Take `p>N`. For indices `0<=i,j<N`, every nonzero difference satisfies

\[
0<|i-j|<N<p,
\]

so `p` cannot divide `i-j`. Therefore

\[
(B_p^{(N)})_{i,j}
=
\begin{cases}
p-1,&i=j,\\
-1,&i\ne j,
\end{cases}
\]

and hence

\[
\boxed{B_p^{(N)}=pI_N-J_N.}
\tag{2}
\]

No asymptotic estimate or large-sieve input is involved. Equation (2) is simply the prime Ramanujan-sum identity observed on a window shorter than one period.

This is the opposite extreme from WI-080's complete-period orthogonal-projector picture. On a complete `p`-period, the primitive-frequency block resolves a `p-1` dimensional exact-period subspace. On an `N<p` consecutive window, every such prime block collapses into the same two-dimensional matrix span

\[
\operatorname{span}\{I_N,J_N\}.
\tag{3}
\]

The modulus survives only through the coefficient multiplying `I_N`.

## 2. All large-prime signed scalar combinations have an exact two-eigenvalue spectrum

Let `P` be any finite set of primes greater than `N`, with real coefficients `omega_p`. Using (2),

\[
\begin{aligned}
A_\omega^{(N)}
&=\sum_{p\in P}\omega_p(pI_N-J_N)\\
&=aI_N-bJ_N,
\end{aligned}
\tag{4}
\]

where

\[
\boxed{
a:=\sum_{p\in P}p\omega_p,
\qquad
b:=\sum_{p\in P}\omega_p.
}
\tag{5}
\]

Since `J_N` vanishes on the codimension-one space `1^perp` and acts by `N` on the constant vector, the spectrum is exactly

\[
\boxed{
\operatorname{spec}(A_\omega^{(N)})
=\{a\text{ with multiplicity }N-1,\ a-Nb\text{ with multiplicity }1\}.
}
\tag{6}
\]

Thus the inertia is obtained by reading the signs of `a` and `a-Nb`; no finer information about the individual prime blocks remains at scalar-operator level.

For `N>=2`, equation (6) also gives the exact zero criterion

\[
\boxed{
A_\omega^{(N)}=0
\quad\Longleftrightarrow\quad
a=0\text{ and }b=0.
}
\tag{7}
\]

So two independent signed moments are not merely necessary tests in this large-prime regime; they are a complete set of invariants for the finite operator.

This sharpens WI-079's entrywise Ramanujan/divisor-marginal gates in one concrete region. There the general operator can carry many independent arithmetic marginals. Here every lag `1<=|h|<N` sees the same value `-sum omega_p`, while the diagonal sees `sum (p-1)omega_p=a-b`; after (5), all those conditions collapse to the same two-dimensional ledger.

## 3. Three primes give perfect cancellation with both sign dictionaries saturated

Choose distinct primes

\[
N<p<q<r
\]

and define

\[
\omega_p=r-q,
\qquad
\omega_q=p-r,
\qquad
\omega_r=q-p.
\tag{8}
\]

These coefficients are all nonzero and have sign pattern `+,-,+`. Their unweighted sum is

\[
(r-q)+(p-r)+(q-p)=0.
\tag{9}
\]

Their prime-weighted sum is also exactly zero:

\[
\begin{aligned}
p(r-q)+q(p-r)+r(q-p)
&=pr-pq+pq-qr+qr-pr\\
&=0.
\end{aligned}
\tag{10}
\]

Equations (7), (9), and (10) give

\[
\boxed{
(r-q)B_p^{(N)}+(p-r)B_q^{(N)}+(q-p)B_r^{(N)}=0.
}
\tag{11}
\]

The example is already beyond every undercomplete protection in WI-082. The positive primitive-frequency count is

\[
K_+=\varphi(p)+\varphi(r)=p+r-2>N,
\tag{12}
\]

and the negative count is

\[
K_-=\varphi(q)=q-1\ge N,
\tag{13}
\]

because `q>N`. Hence both sign-side dictionaries span the full `N`-sample space by the Vandermonde argument of WI-082, while their weighted indefinite Gram combination nevertheless vanishes identically.

Equivalently, in WI-082's factorization

\[
A_\omega^{(N)}=WJW^*,
\]

the `N`-dimensional image `E=ran W^*` is a totally isotropic subspace for the ambient signature form `J`: the restriction of the Hermitian form to `E` is exactly zero. Thus WI-082's statement that the doubly saturated regime is not controlled by dimension alone is sharp in the strongest possible sense. The maximum possible nullity `n_0(A)=N` is attained by an explicit three-modulus prime family.

## 4. Consequence for the scalar escape after WI-082

WI-079--WI-082 progressively showed that:

- an ordinary positive sparse-moduli large sieve discards the signs;
- complete-period Ramanujan blocks do not cancel across distinct moduli;
- pairwise finite-window rank leakage is often maximal; and
- before overcompleteness, Vandermonde congruence fixes the full inertia sign ledger.

WI-082 therefore left the doubly saturated regime `K_+>=N`, `K_->=N` as the first place where a genuinely metric/weighted signed scalar mechanism could still operate. Equation (11) shows that this is not merely a gap in the lower bounds. **Exact complete cancellation really occurs in the universal scalar Ramanujan model.**

Accordingly, there can be no theorem of the form

\[
\boxed{
\text{doubly saturated signed Ramanujan finite section}
\quad\Longrightarrow\quad
\text{nonzero residual inertia}
}
\tag{14}
\]

under only the generic hypotheses retained by WI-079--WI-082. Nor can an arbitrary positive lower bound on `||A_omega^(N)||`, rank, or either inertia sign follow solely from the presence of both sign families and their primitive-frequency multiplicities: the left side of (11) has all of those ingredients and is exactly zero.

The next useful scalar invariant must therefore be **source specific**. For a proposed Yang reduction, one must determine whether its actual aggregated coefficients can approach or satisfy cancellation in the relevant moment directions, whether its active moduli lie in a regime where the collapse (2) is present, and what additional coefficient/factorization labels constrain the allowed signed measure. A theorem exploiting those restrictions would be genuinely stronger information than universal finite-window Ramanujan geometry.

This also argues against spending more effort on generic pairwise rank refinements in the doubly saturated regime. Rank has already ceased to be the relevant resource: the individual sign dictionaries can each have full sample rank while the signed weighted operator is identically zero.

## 5. Classical prior art and novelty boundary

No novelty is claimed for the prime Ramanujan-sum values (1), the Fourier representation of Ramanujan sums, or the exact-period Ramanujan-subspace framework. The structural background is already anchored in `SOURCES.md`:

- Noboru Ushiroya, **Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums**, *Journal of Integer Sequences* 21 (2018), Article 18.2.6; arXiv:1803.02970. WI-080 uses its common-period convolution orthogonality and Ramanujan-matrix spectral results.
- P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals** and **Part II: FIR Representations and Applications**, *IEEE Transactions on Signal Processing* 62 (2014). WI-080 uses this as the classical exact-period/Ramanujan-subspace framework.

The closely related classical identity

\[
\sum_{d\mid Q}c_d(h)
=
\begin{cases}
Q,&Q\mid h,\\
0,&Q\nmid h
\end{cases}
\tag{15}
\]

also implies, for every `Q>N`,

\[
\sum_{d\mid Q}B_d^{(N)}=QI_N.
\tag{16}
\]

Equation (16) is another way to see that short finite windows create many exact linear dependencies between Ramanujan blocks. The three-prime relation (11) is stronger for the present audit because it stays entirely inside prime moduli and avoids introducing the modulus-one block or a divisor family.

A bounded novelty audit of the current `weil_inertia` corpus found WI-079's general Ramanujan operator, WI-080's complete-period projectors, WI-081's finite-section pairwise ranks, and WI-082's global Vandermonde congruence, but no stored finding giving the large-prime collapse (2) or an explicit doubly saturated zero operator such as (11). **No priority claim is made.** The durable Mathia content is the application of these elementary classical identities to the exact scalar interface left open by WI-082, showing that its doubly saturated boundary admits perfect cancellation rather than merely lacking a generic lower bound.

No `SOURCES.md` change is needed because the load-bearing external Ramanujan-subspace sources are already recorded there and the new step is exact finite algebra.

## 6. Boundary conditions and counterarguments

1. **This is an interface counterexample, not a Yang source counterexample.** Mathia has still not proved that the full post-local-main Yang locked covariance reduces exactly to a signed scalar operator of the WI-079 form. Equation (11) therefore cannot be read as a failure of the Yang covariance itself.
2. **The prime moduli must exceed the sample window.** The collapse (2) uses `p>N`. For primes at or below `N`, nonzero sampled lags can be divisible by `p`, so additional periodic structure survives and the operator need not lie in `span{I,J}`.
3. **The coefficients are freely chosen.** The three-prime weights (8) prove existence inside the universal scalar model. The actual Yang coefficient law may forbid these weights, their signs, or the required moment cancellation. Establishing such a restriction is exactly the source-specific information now required.
4. **No lower bound for all overcomplete scalar families is possible, but restricted families may still be rigid.** Positivity, monotonicity, factorization constraints, source normalization, fixed signs, or arithmetic identities among the true coefficients can exclude (11). Any future theorem must state and use those restrictions explicitly.
5. **Source-labelled and multidimensional transforms remain live.** The relation occurs only after collapse to scalar modulus blocks. A representation retaining reduced directions, pair labels, residue fibers, or the exact locked four-prime geometry can distinguish configurations identified by (2).
6. **Operator cancellation is stronger than inertia cancellation but narrower than the original zeta problem.** The example proves `A=0` inside the scalar interface. It says nothing directly about off-critical zero blocks, multiplicity, the Montgomery--Taylor Gram defect, or the certified simple-critical proportion.
7. **No new arithmetic theorem is used.** All load-bearing equalities are finite and exact; the prior-art role is only to situate Ramanujan sums/subspaces as classical structure.

## 7. Consequence for the research program

The scalar-obstruction chain now has a sharp phase transition. In the undercomplete regime, WI-082 proves that finite-window mixing cannot erase any sign direction. In the overcomplete regime, the present finding shows that universal scalar geometry can erase **all** of them:

\[
\boxed{
K\le N
\Rightarrow
\text{signature fixed by congruence},
\qquad
K_+,K_-\ge N
\centernot\Rightarrow
\text{any residual signature at all}.
}
\tag{17}
\]

The cheapest decisive test for a future signed scalar Yang proposal is therefore no longer another universal rank estimate. After exact coefficient aggregation, test the **actual source coefficient moments and modulus scales** against the finite-window operator they generate. If a large-prime portion is present, equations (4)--(7) reduce that portion exactly to the two ledgers `sum omega_p` and `sum p omega_p`; if the source forbids their cancellation, that is new usable structure. If it does not, scalarization has already discarded enough information to permit perfect cancellation.

A source-faithful theorem that survives this test must use coefficient laws, factorization/direction labels, or genuinely multidimensional covariance information. The exact three-prime witness closes the cheaper hope that doubly saturated scalar Ramanujan blocks retain a universal inertia obstruction after WI-082.