# WI-086 — Pairwise Ramanujan rank defect starts only after the boundary exceeds both totient dimensions

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not repair or certify the Yang--Yang one-sided fourth-moment candidate. It resolves the pairwise-rank question raised by `CLUE-cyclotomic-transversality-pairwise-rank`: the universal sharpness range in WI-081 extends from the smaller totient dimension to the larger one, and every remaining defect is exactly an excess subspace-intersection dimension. Cyclotomic divisibility gives an exact normal form for that defect, but by itself supplies no stronger universal rank bound.

Let

\[
U_m^{(N)}=(e(ax/m))_{0\le x<N,\ a\in(\mathbf Z/m\mathbf Z)^\times},
\qquad
G_{m,n}^{(N)}=(U_m^{(N)})^*U_n^{(N)},
\]

for distinct positive moduli `m,n`. As in WI-081, put

\[
\ell=\operatorname{lcm}(m,n),\qquad
r=N\bmod\ell,\qquad
\delta=\delta_N(m,n):=\min\{r,\ell-r\}.
\]

Write

\[
a=\varphi(m),\qquad b=\varphi(n).
\]

Then the strengthened universal rank statement is

\[
\boxed{
\delta\le\max\{a,b\}
\quad\Longrightarrow\quad
\operatorname{rank}G_{m,n}^{(N)}
=\min\{\delta,a,b\}.
}
\tag{1}
\]

Thus a genuinely exceptional pairwise rank deficiency cannot occur merely when the boundary length first exceeds the **smaller** Ramanujan dimension. It can begin only in the complementary regime

\[
\boxed{\delta>\max\{\varphi(m),\varphi(n)\}.}
\tag{2}
\]

In that remaining regime, suppose without loss of generality that `a<=b`. Let

\[
V_m=V_m^{(\delta)}:\mathbf C^a\to\mathbf C^\delta,
\qquad
V_n=V_n^{(\delta)}:\mathbf C^b\to\mathbf C^\delta
\]

be the consecutive primitive-root Vandermonde matrices from WI-081, and set

\[
\mathcal U=\operatorname{ran}V_m,
\qquad
\mathcal W=\operatorname{ran}V_n.
\]

Because `delta>b>=a`, both have full column rank. Define

\[
\boxed{
\tau_{m,n}(\delta)
:=\dim(\mathcal W\cap\mathcal U^\perp)-(b-a).
}
\tag{3}
\]

Then

\[
\boxed{
\tau_{m,n}(\delta)
=\dim(\mathcal U\cap\mathcal W^\perp)\ge0,
\qquad
\operatorname{rank}G_{m,n}^{(N)}=a-\tau_{m,n}(\delta).
}
\tag{4}
\]

So every exceptional rank loss is exactly the **excess transversality defect** beyond the intersection dimension already forced by ambient linear algebra.

Moreover, identify a vector `f=(f_0,...,f_{delta-1})` with

\[
F_f(X)=\sum_{x=0}^{\delta-1}f_xX^x.
\]

Then

\[
\boxed{
f\in\mathcal U^\perp
\quad\Longleftrightarrow\quad
\Phi_m(X)\mid F_f(X)\ \text{in }\mathbf C[X],
}
\tag{5}
\]

where `Phi_m` is the `m`-th cyclotomic polynomial. Consequently

\[
\boxed{
\tau_{m,n}(\delta)
=
\dim\{f\in\mathcal W:\Phi_m\mid F_f\}-(b-a).
}
\tag{6}
\]

Equation (6) is an exact arithmetic representation of the only remaining pairwise defect, but it is not by itself a new saving: divisibility by `Phi_m` is exactly the coordinate description of the already-known orthogonal complement `U^perp`. A useful continuation must exploit additional restrictions on membership in `W`, the actual source coefficients, singular values, simultaneous interactions among several moduli, or source labels discarded by scalar Ramanujan reduction.

## 1. WI-081's shorter-boundary factorization reduces the problem to two rectangular Vandermonde maps

WI-081 proves that cancellation of complete `lcm(m,n)` periods and, when needed, passage to the translated complementary boundary give, up to an overall sign and invertible diagonal phase factors,

\[
G_{m,n}^{(N)}\sim (V_m^{(\delta)})^*V_n^{(\delta)}.
\tag{7}
\]

The phase factors do not change rank. The columns of `V_q^(delta)` are the sequences

\[
(1,\zeta,\zeta^2,\ldots,\zeta^{\delta-1})^T
\]

as `zeta` ranges over the distinct primitive `q`-th roots of unity.

For arbitrary distinct nodes, the ordinary rectangular Vandermonde argument gives

\[
\boxed{
\operatorname{rank}V_q^{(\delta)}
=\min\{\delta,\varphi(q)\}.
}
\tag{8}
\]

Indeed, if `delta<=phi(q)`, select any `delta` columns and use the nonzero square Vandermonde determinant to get full row rank. If `delta>=phi(q)`, use the first `phi(q)` rows to get a square Vandermonde matrix with nonzero determinant and hence full column rank. No prime-modulus hypothesis is involved.

WI-081 persisted and formally checked the first consequence of this observation when `delta<=min(a,b)`. The second, one-sided-saturation regime gives the stronger threshold (1).

## 2. One surjective side is enough: the exact `max(phi(m),phi(n))` threshold

Assume `a<=b`; the opposite ordering is symmetric.

If

\[
\delta\le a,
\]

both `V_m` and `V_n` have full row rank `delta`. Hence `V_n:C^b->C^delta` is surjective while `V_m^*:C^delta->C^a` is injective, and

\[
\operatorname{rank}(V_m^*V_n)=\delta.
\tag{9}
\]

This is the small-boundary equality already in WI-081.

Now take the previously untreated range

\[
a<\delta\le b.
\tag{10}
\]

Equation (8) says that `V_n:C^b->C^delta` is still surjective. It also says that `V_m:C^a->C^delta` has full column rank `a`, so its adjoint has rank `a`:

\[
\operatorname{rank}V_m^*=a.
\tag{11}
\]

Surjectivity of `V_n` implies

\[
\operatorname{ran}(V_m^*V_n)
=V_m^*(\operatorname{ran}V_n)
=V_m^*(\mathbf C^\delta)
=\operatorname{ran}V_m^*.
\tag{12}
\]

Therefore

\[
\operatorname{rank}(V_m^*V_n)=a.
\tag{13}
\]

Combining (9) and (13),

\[
\operatorname{rank}G_{m,n}^{(N)}
=\min\{\delta,a\}
=\min\{\delta,a,b\}
\]

throughout `delta<=b=max(a,b)`, proving (1).

This closes a natural pairwise-rank refinement route on a substantially larger region than WI-081's original theorem. Until the boundary length exceeds **both** primitive-frequency dimensions, rank alone is already maximal given the smaller dimension and cannot yield an additional signed-inertia saving.

## 3. In the residual regime, rank loss is exactly excess nontransversality

Continue with `a<=b` and now assume

\[
\delta>b.
\tag{14}
\]

Both Vandermonde maps are injective, with

\[
\dim\mathcal U=a,
\qquad
\dim\mathcal W=b.
\tag{15}
\]

Restrict `V_m^*` to `W`. Its kernel is exactly

\[
\ker(V_m^*|_{\mathcal W})
=\mathcal W\cap\ker V_m^*
=\mathcal W\cap\mathcal U^\perp.
\tag{16}
\]

Because `V_n` is an isomorphism from `C^b` onto `W`, rank-nullity gives

\[
\operatorname{rank}(V_m^*V_n)
=b-\dim(\mathcal W\cap\mathcal U^\perp).
\tag{17}
\]

On the other hand, applying the same argument to the adjoint product gives

\[
\operatorname{rank}(V_m^*V_n)
=a-\dim(\mathcal U\cap\mathcal W^\perp).
\tag{18}
\]

Equating (17) and (18) yields

\[
\dim(\mathcal W\cap\mathcal U^\perp)-(b-a)
=\dim(\mathcal U\cap\mathcal W^\perp).
\tag{19}
\]

This proves (4), including nonnegativity. Equivalently, the forced dimension bound

\[
\dim(\mathcal W\cap\mathcal U^\perp)\ge b-a
\]

accounts for the asymmetric dimensions; only the excess above `b-a` represents exceptional loss of the maximal possible rank `a`.

The generic dimension ceiling also gives

\[
0\le\tau_{m,n}(\delta)\le\min\{a,\delta-b\},
\tag{20}
\]

so

\[
\operatorname{rank}G_{m,n}^{(N)}
\ge\max\{0,a+b-\delta\}.
\tag{21}
\]

Equation (21) is only the classical Sylvester/dimension lower bound; the point of (3)--(4) is to isolate exactly what additional root-of-unity transversality must be controlled to do better.

### The known close-prime witness has `tau=2`

WI-081 proves that for

\[
(p,q,\delta)=(11,13,47)
\]

one has

\[
\operatorname{rank}G=8.
\]

Here

\[
a=\varphi(11)=10,
\qquad
b=\varphi(13)=12.
\]

Thus

\[
\dim(\mathcal W\cap\mathcal U^\perp)=b-\operatorname{rank}G=4,
\]

whereas the dimension-forced baseline is `b-a=2`. Hence

\[
\boxed{\tau_{11,13}(47)=2.}
\tag{22}
\]

The exceptional rank-eight example is therefore exactly a two-dimensional excess-transversality event in the new ledger.

## 4. Cyclotomic divisibility is the exact polynomial normal form

Let `f in C^delta` and

\[
F_f(X)=\sum_{x=0}^{\delta-1}f_xX^x.
\]

For a primitive `m`-th root `zeta`, the corresponding coordinate of `V_m^* f` is

\[
\sum_{x=0}^{\delta-1}\overline{\zeta^x}f_x
=\sum_{x=0}^{\delta-1}f_x\zeta^{-x}
=F_f(\zeta^{-1}),
\tag{23}
\]

because every root of unity has unit modulus. Inversion permutes the primitive `m`-th roots. Therefore

\[
V_m^*f=0
\iff
F_f(\zeta)=0\quad\text{for every primitive }m\text{-th root }\zeta.
\tag{24}
\]

The primitive roots are precisely the simple roots of the cyclotomic polynomial `Phi_m`. Hence over `C[X]`,

\[
V_m^*f=0
\iff
\Phi_m\mid F_f,
\tag{25}
\]

proving (5). A translated consecutive boundary multiplies Vandermonde columns by nonzero root-of-unity phases, so it changes neither the sampled subspace nor this kernel criterion after the harmless phase normalization already used in WI-081.

Combining (25) with (3) gives (6). This is a clean way to encode exceptional pairwise defects, but it must not be overinterpreted. The space

\[
\{F:\deg F<\delta,\ \Phi_m\mid F\}
\]

already has dimension `delta-a`, exactly matching `dim U^perp`. Thus the divisibility condition alone contains no information beyond orthogonality to the `m`-block. The difficult part is the simultaneous requirement that the coefficient vector belong to the primitive `n`-frequency span `W`.

Consequently, merely replacing the subspace intersection by the words "cyclotomic divisibility" is a reparameterization, not a new mechanism. Any sharper theorem must constrain the intersection using additional arithmetic of the two root sets, the source's actual coefficient law, simultaneous multi-modulus consistency, metric/singular-value information, or a representation retaining labels lost by scalarization.

## 5. Relation to the later scalar Ramanujan obstruction chain

This result sharpens WI-081 but does not reopen the universal scalar route closed by WI-082--WI-085.

- WI-082 shows that many-family inertia is fixed by congruence only before the global primitive-frequency dictionary becomes overcomplete.
- WI-083 gives exact signed cancellation in a doubly saturated super-window family.
- WI-084 proves that the subwindow blocks `B_1^(N),...,B_N^(N)` are nevertheless an exact Toeplitz basis.
- WI-085 identifies the complete `N`-coordinate alias quotient for arbitrary scalar moduli.

The present theorem concerns a **two-block cross Gram before scalar weighted aggregation**. It says that pairwise rank deficiency itself has an even narrower universal support than WI-081 recorded: exceptional deficiency requires `delta>max(phi(m),phi(n))`. But once a source is scalarized into the quotient of WI-085, pairwise transversality cannot recover labels that the quotient has already erased.

So the research consequence is negative but useful. Generic pairwise rank improvements should not be pursued in the region `delta<=max(phi(m),phi(n))`, where exact maximality is now proved. In the residual region, a useful source-sensitive invariant must control `tau` rather than merely restate it.

## 6. Prior art and novelty boundary

The load-bearing ingredients are classical or already persisted.

- Ordinary rectangular Vandermonde rank for distinct nodes gives (8). No novelty is claimed for this linear-algebra fact.
- P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals**, *IEEE Transactions on Signal Processing* 62 (2014), 4145--4157, DOI `10.1109/TSP.2014.2331617`, develops Ramanujan subspaces through primitive periodic/Fourier structure.
- P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part II: FIR Representations and Applications**, *IEEE Transactions on Signal Processing* 62 (2014), 4158--4172, DOI `10.1109/TSP.2014.2331624`, treats finite-duration Ramanujan representations and orthogonal periodic-subspace decompositions.
- WI-081 supplies the nearest-LCM boundary factorization (7), its exact `delta<=min(a,b)` theorem, prime refinements, and the `(11,13,47)` certificate. `research/weil_inertia/formalization/WI081PairwiseRamanujanRank.lean` kernel-checks the boundary upper bound and the original small-boundary equality, but **does not yet formalize** the stronger threshold (1), the transversality ledger (3)--(4), or the cyclotomic normal form (5)--(6).
- Cyclotomic polynomials as the monic polynomials whose roots are exactly the primitive roots of unity, and the equivalence between vanishing on all those roots and divisibility over `C[X]`, are classical.

A bounded prior-art search around finite-duration Ramanujan subspaces, partial Fourier/Vandermonde matrices, primitive-root subspace intersections, and cyclotomic divisibility located the standard Ramanujan-subspace and Fourier/Vandermonde frameworks, but did not locate a source stating this specific nearest-LCM `delta<=max(phi(m),phi(n))` consequence or the `tau` bookkeeping in the WI-081 setting. **No priority claim is made.** The durable Mathia content is the exact specialization of classical rectangular-Vandermonde and rank-nullity facts to WI-081's shorter-boundary factorization, together with the conclusion that the proposed cyclotomic representation is exact but not itself a stronger universal invariant.

No `SOURCES.md` change is needed: Vaidyanathan's Ramanujan-subspace framework is already a durable source anchor for the WI-080--WI-085 chain, while the new load-bearing steps are elementary finite linear algebra and cyclotomic algebra.

## 7. Boundary conditions and falsification

1. **Distinct positive moduli are required for the WI-081 boundary factorization.** The argument inherits its nontrivial cross-frequency/root-of-unity cancellation hypotheses.
2. **The theorem is pairwise.** It does not by itself control simultaneous cancellation among three or more modulus families, signed scalar combinations, or the full Yang covariance.
3. **`delta<=max(a,b)` is a sufficient maximal-rank region, not a claim that every `delta>max(a,b)` pair is deficient.** The latter regime merely permits nonzero `tau`; many pairs can still have `tau=0`.
4. **Cyclotomic divisibility is exact only after fixing the ordinary coefficient-vector identification and Hermitian convention.** Inversion of primitive roots and translated-boundary phases are harmless, but they must not be confused with an extra arithmetic constraint.
5. **The `(11,13,47)` example checks the ledger but does not classify the residual regime.** It proves that nonzero `tau` really occurs, not that close primes are the only source.
6. **No zeta analytic input enters.** The result narrows a possible finite-dimensional mechanism inside the Yang/Ramanujan audit but yields no simple-zero proportion improvement on its own.
7. **A counterexample to (1) under WI-081's exact factorization would refute the finding.** Because the proof reduces to ordinary full rectangular Vandermonde rank and surjectivity, such a counterexample would have to expose a convention/factorization error rather than a subtle number-theoretic exception.

## 8. Consequence for the research program

The pairwise finite-window phase diagram is now sharper:

\[
\boxed{
\delta\le\max\{\varphi(m),\varphi(n)\}
\Longrightarrow
\text{maximal possible pairwise rank},
}
\]

whereas

\[
\boxed{
\delta>\max\{\varphi(m),\varphi(n)\}
\Longrightarrow
\operatorname{rank}G=\min\{\varphi(m),\varphi(n)\}-\tau
}
\]

with `tau` the exact excess-transversality dimension.

This kills the cheap hope that the gap between WI-081's old `min(phi(m),phi(n))` threshold and the larger totient dimension hides a generic pairwise rank saving. It also settles the first-order value of the proposed cyclotomic reformulation: it is a useful exact coordinate system for the residual defect, but **not** a new bound without source-specific structure.

A productive continuation would therefore begin only after exact Yang coefficient/source aggregation and ask whether its admissible modulus pairs or coefficient laws force `tau=0`, bound `tau`, or couple several `tau` defects in a way incompatible with the scalar alias quotient of WI-085. Generic pairwise Vandermonde rank is exhausted before that point.