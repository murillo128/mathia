# PL-203 — Injective dense-range noninvertible prime-edge weights still do not force arithmetic rigidity

**Status:** negative result / structural collapse  
**Evidence class:** EXACT-DERIVED + LITERATURE-ADJACENT + DECISIVE-NEGATIVE  
**Research line:** `prime_lattice`

## Claim

The singular/noninvertible escape left open by `PL-202` does not become arithmetically rigid merely because the prime-edge weights fail to have bounded inverses. Even if **every** edge weight is bounded, injective, has dense range, is non-surjective, and the family satisfies exact prime-square flatness and exact resolvent covariance, an arbitrary uniformly bounded self-adjoint spectral field can still be embedded as a reducing summand.

Let

\[
\Gamma=\mathbb N_0^{(\mathcal P)},
\qquad
|\alpha|=\sum_p\alpha_p,
\]

and let \(\mathcal K_0\) be any Hilbert space. Choose an arbitrary uniformly bounded self-adjoint field

\[
B_\alpha=B_\alpha^*\in\mathcal B(\mathcal K_0),
\qquad
\sup_{\alpha\in\Gamma}\|B_\alpha\|\le M.
\]

On \(\ell^2(\mathbb N)\), let

\[
De_k=k e_k
\]

with its standard positive self-adjoint domain, and put

\[
\mathcal K=\mathcal K_0\oplus\ell^2(\mathbb N),
\qquad
H_\alpha=B_\alpha\oplus D^{|\alpha|+1}.
\]

Then

\[
H=\bigoplus_{\alpha\in\Gamma}H_\alpha
\]

is self-adjoint on its natural direct-sum domain. Write

\[
R=(H-i)^{-1}=\bigoplus_\alpha R_\alpha.
\]

For the canonical source prime shifts

\[
V_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes\xi,
\]

define target edge weights by the block formulas

\[
A_p^B(\alpha)
 =(B_{\alpha+e_p}-i)^{-1}(B_\alpha-i)
\]

and

\[
A_p^D(\alpha)e_k
 =\frac{k^{|\alpha|+1}-i}{k^{|\alpha|+2}-i}\,e_k.
\]

Set

\[
A_p(\alpha)=A_p^B(\alpha)\oplus A_p^D(\alpha),
\]

and

\[
T_p(\delta_\alpha\otimes\xi)
 =\delta_{\alpha+e_p}\otimes A_p(\alpha)\xi.
\]

Then:

\[
\boxed{RV_p=T_pR\qquad\forall p,}
\]

\[
\boxed{T_pT_q=T_qT_p\qquad\forall p,q,}
\]

and

\[
\boxed{
\sup_{p,\alpha}\|A_p(\alpha)\|<\infty.
}
\]

Every \(A_p(\alpha)\) is injective with dense range but is not surjective and has no bounded inverse. Nevertheless the reducing \(\mathcal K_0\)-summand contains the completely arbitrary field \(\{B_\alpha\}\). Thus **noninvertibility by itself supplies no RH-sensitive rigidity**. Any surviving singular-weight mechanism must make an actual kernel, cokernel/range defect, support defect, domain defect, irreducibility constraint, or other singular structure load-bearing and arithmetically forced rather than merely attach a generic noninvertible tail.

## 1. The singular tail is genuinely noninvertible but remains dense-range

For \(d=|\alpha|\), the tail coefficient is

\[
a_d(k)=\frac{k^{d+1}-i}{k^{d+2}-i}.
\]

Since \(k\ge1\),

\[
|a_d(k)|^2
 =\frac{k^{2d+2}+1}{k^{2d+4}+1}
 \le1,
\]

so \(\|A_p^D(\alpha)\|\le1\) uniformly. Every coefficient is nonzero, hence the diagonal operator is injective. Finite-support sequences lie in its range, so the range is dense.

On the other hand,

\[
|a_d(k)|\sim \frac1k
\qquad(k\to\infty),
\]

so \(A_p^D(\alpha)\) is not bounded below. In particular it has no bounded inverse and its range is not closed. It is also not onto: for example \(y=(1/k)_{k\ge1}\in\ell^2\), while the formal preimage \(y_k/a_d(k)\) tends to \(1\) and hence is not in \(\ell^2\).

The \(B\)-block is uniformly bounded because

\[
\|(B_{\alpha+e_p}-i)^{-1}\|\le1,
\qquad
\|B_\alpha-i\|\le\sqrt{M^2+1}.
\]

Therefore

\[
\|A_p(\alpha)\|
 \le\max\{\sqrt{M^2+1},1\}
\]

for all \(p,\alpha\). Since the tail block is injective dense-range non-surjective, so is the total edge operator, despite the first block being invertible.

## 2. Exact resolvent covariance survives the singularity

On the arbitrary bounded block, write

\[
R_\alpha^B=(B_\alpha-i)^{-1}.
\]

Then by definition

\[
A_p^B(\alpha)R_\alpha^B
 =R_{\alpha+e_p}^B.
\]

On the tail block,

\[
R_\alpha^D e_k
 =\frac1{k^{|\alpha|+1}-i}e_k,
\]

and hence

\[
A_p^D(\alpha)R_\alpha^D e_k
 =\frac{k^{|\alpha|+1}-i}{k^{|\alpha|+2}-i}
   \frac1{k^{|\alpha|+1}-i}e_k
 =R_{\alpha+e_p}^D e_k.
\]

Thus, as bounded operators,

\[
A_p(\alpha)R_\alpha=R_{\alpha+e_p}.
\]

After inserting the lattice coordinate this is exactly

\[
RV_p=T_pR.
\]

No manipulation of the unbounded inverse \((R_\alpha^D)^{-1}=D^{|\alpha|+1}-i\) is required at the global operator level; the displayed diagonal ratio is already bounded. Hence the covariance statement is domain-safe.

## 3. Exact prime-square flatness also survives

The arbitrary bounded block telescopes endpoint-to-endpoint:

\[
A_q^B(\alpha+e_p)A_p^B(\alpha)
 =(B_{\alpha+e_p+e_q}-i)^{-1}(B_\alpha-i),
\]

which is symmetric in \(p,q\).

For the tail block, the weight depends on the vertex only through \(d=|\alpha|\). Therefore both two-step paths multiply by

\[
\frac{k^{d+1}-i}{k^{d+2}-i}
\frac{k^{d+2}-i}{k^{d+3}-i}
 =\frac{k^{d+1}-i}{k^{d+3}-i}.
\]

Consequently

\[
A_q(\alpha+e_p)A_p(\alpha)
 =A_p(\alpha+e_q)A_q(\alpha),
\]

so \(T_pT_q=T_qT_p\) exactly. This is a genuinely singular flat multishift: the failure of bounded invertibility does not create curvature, and it does not couple the singular tail to the programmable spectral summand.

## 4. What this controls beyond PL-202

`PL-202` showed that invertible operator-valued flat prime weights integrate to a vertex gauge and that exact self-adjoint-resolvent covariance can carry an arbitrary uniformly bounded self-adjoint field. It deliberately left singular/noninvertible weights open because the division step used to recover the vertex gauge can fail.

The present construction shows that **failure of that division step is not itself enough**. One can append to any programmable bounded field a universal degree-dependent singular tail that makes every edge weight injective, dense-range, non-surjective, and non-boundedly-invertible while leaving all exact covariance and flat-square identities intact. The singularity is therefore an inert decoration unless additional hypotheses force it to interact with the arithmetic component.

This is a matched genericity control. The construction uses only the free commutative monoid \(\Gamma\) and its total degree \(|\alpha|\). It does not use the numerical prime labels, \(\log p\), analytic continuation, the functional equation, Möbius cancellation, or Riemann zeros. The same counterexample works after relabeling the generators, including generalized-prime/Beurling analogues. Therefore a positive theorem based only on “flat prime shifts with noninvertible dense-range weights” would not distinguish the ordinary primes from a generic free multiplicative system.

## 5. Prior-art and novelty audit

Noninvertible but injective dense-range operator weights are standard in weighted-shift theory. Jakub Kośmider, “On unitary equivalence of bilateral operator valued weighted shifts,” *Opuscula Mathematica* **39**(4) (2019), 543–555, DOI `10.7494/OpMath.2019.39.4.543`, studies bilateral operator-valued shifts under quasi-invertible-weight hypotheses and supplies close background for this class of singular weights.

Michał Buchała, “Unitarily equivalent bilateral weighted shifts with operator weights,” *Opuscula Mathematica* **44**(5) (2024), 651–672, DOI `10.7494/OpMath.2024.44.5.651`, gives a modern treatment of unitary equivalence for bilateral operator-weighted shifts with quasi-invertible weights. These sources delimit the operator-theory background; they do not provide an arithmetic/RH rigidity result or the prime-lattice resolvent construction above.

The nearby invertible multishift literature cited in `PL-202`—Gupta, Kumar, and Trivedi (2020), and Ghara, Kumar, and Trivedi (2024)—covers commuting operator-valued multishifts and similarity when weights are invertible. It does not invalidate the singular-tail control because the new edge weights deliberately fail bounded invertibility.

Accordingly, no novelty is claimed for operator-valued weighted shifts, quasi-invertible/dense-range weights, or their unitary-equivalence theory. The durable line-specific delta is the explicit **self-adjoint resolvent counterconstruction** showing that the weak singular escape left by `PL-202` remains fully programmable after adjoining an injective dense-range noninvertible tail. The proof is elementary and self-contained; the literature is used only to delimit novelty, so no `SOURCES.md` update is required.

## 6. Adversarial boundaries

This negative control is intentionally narrow. It does **not** show that arbitrary singular flat weights integrate to a global gauge, nor does it rule out singular weights whose kernel or range geometry is itself arithmetically forced. In particular, weights with nontrivial kernels, nondense ranges, finite-rank or rank-varying defects, support-changing defects, or topological index data remain outside the construction.

It also does not rule out an irreducibility/minimality hypothesis that forbids the direct-sum separation used here. Such a hypothesis would have to arise naturally from the completed-zeta/prime-lattice problem rather than be imposed solely to exclude this counterexample. Likewise, unbounded transports, domain-changing covariance, approximate or ideal-valued relations, target-relative compressions, and genuinely noncommuting source actions remain separate regimes.

A particularly important distinction is that the arbitrary field \(B_\alpha\) is embedded as a **reducing summand** of \(H_\alpha\); the construction does not claim that every singular resolvent-covariant field is programmable as the entire fiber operator. That weaker embedding statement is already enough to refute noninvertibility alone as a rigidity principle, because any candidate invariant that ignores the decoupled programmable summand can be altered arbitrarily without changing the singular tail.

## Consequence for the research line

The operator-valued escape is now narrower than after `PL-202`. The progression is:

\[
\text{unitary flat weights}
\to
\text{invertible nonunitary flat weights}
\to
\text{injective dense-range noninvertible flat weights},
\]

and none of these hypotheses by themselves forces arithmetic spectral content.

The surviving singular route must therefore make the **defect** itself the arithmetic object. A viable mechanism would need, for example, a prime-dependent kernel/cokernel or range-support pattern, an index or defect space with nontrivial compatibility across prime squares, or a domain singularity that cannot be split off from the zeta-sensitive component. Merely replacing invertible weights by dense-range noninvertible ones does not provide the missing RH rigidity.