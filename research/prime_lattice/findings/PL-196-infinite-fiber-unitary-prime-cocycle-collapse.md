# PL-196 — Exact unitary prime cocycles collapse for arbitrary Hilbert fibers

**Status:** negative result / structural collapse  
**Evidence class:** EXACT-DERIVED + LITERATURE-ADJACENT + DECISIVE-NEGATIVE  
**Research line:** `prime_lattice`

## Claim

Let

\[
\mathcal H=\ell^2(\mathbb N)\otimes\mathcal K
\]

for an arbitrary complex Hilbert space `K`, with no finite-dimensionality or separability assumption on the internal fiber. Let

\[
V_p=S_p\otimes I_{\mathcal K},
\qquad S_p e_n=e_{pn}.
\]

Let `L=L^*` be a possibly unbounded self-adjoint operator on `H`, put

\[
R=(L-i)^{-1},
\]

and suppose that for every rational prime `p` there is a unitary `U_p` on `K` such that

\[
\boxed{
R V_p=(S_p\otimes U_p)R.
}
\]

Then

\[
\boxed{U_p=I_{\mathcal K}\qquad\text{for every prime }p.}
\]

After this collapse there is a self-adjoint operator `K_0` on the internal Hilbert space `K` such that

\[
\boxed{
L=I_{\ell^2(\mathbb N)}\otimes K_0,
\qquad
R=I_{\ell^2(\mathbb N)}\otimes(K_0-i)^{-1}.
}
\]

Thus even an infinite-dimensional internal space with continuous unitary spectrum does not rescue exact unitary prime-shift covariance. Any remaining spectrum is carried entirely by an inert internal factor and is repeated independently of the exponent lattice. The prime directions contribute no nontrivial cocycle and no zero-sensitive spectral coupling.

This strictly extends the finite-fiber no-go in `PL-195`. Finite dimensionality was essential to the trace/eigenvector proof used there, but not to the theorem itself: a mean-ergodic argument removes the continuous-spectrum loophole.

## 1. One prime already forces its entire unitary cocycle to be trivial

Fix a prime `p` and abbreviate

\[
V=S_p\otimes I,
\qquad
W=S_p\otimes U,
\qquad
\widetilde U=I\otimes U.
\]

The assumed covariance is

\[
RV=WR.
\]

Both `V` and `W` are isometries. Iterating and then compressing by `V^{*k}` gives, for every integer `k>=0`,

\[
R V^k=W^kR
\]

and hence

\[
V^{*k}RV^k
=V^{*k}W^kR
=(I\otimes U^k)R
=\widetilde U^kR.
\]

For a self-adjoint resolvent at `i`,

\[
\boxed{
\operatorname{Im}R=R^*R.
}
\]

Indeed `R-R^*=2iR^*R`. Therefore

\[
\begin{aligned}
\operatorname{Im}(\widetilde U^kR)
&=V^{*k}(\operatorname{Im}R)V^k\\
&=V^{*k}R^*RV^k\\
&=(RV^k)^*(RV^k)\\
&=(W^kR)^*(W^kR)\\
&=R^*R.
\end{aligned}
\]

Thus the entire unitary orbit has the same positive imaginary part:

\[
\boxed{
\operatorname{Im}(\widetilde U^kR)=R^*R
\qquad(k\ge0).
}
\]

This identity replaces the finite-dimensional eigenphase argument of `PL-195`.

## 2. Mean ergodicity kills continuous unitary spectrum as well

Let

\[
A_N=\frac1N\sum_{k=0}^{N-1}\widetilde U^k.
\]

By the von Neumann mean ergodic theorem for a unitary operator,

\[
A_N\longrightarrow P
\]

strongly, where `P` is the orthogonal projection onto the fixed space

\[
\ker(\widetilde U-I)
=\ell^2(\mathbb N)\otimes\ker(U-I).
\]

The adjoint Cesaro means converge strongly to the same `P`. Averaging the preceding imaginary-part identity and passing to the strong limit therefore yields

\[
\boxed{
\operatorname{Im}(PR)=R^*R.
}
\]

Put `Q=I-P` and take any `x in QH`. Since `PRx` belongs to `PH` while `x` belongs to `QH`,

\[
\langle PRx,x\rangle=0.
\]

Consequently

\[
\|Rx\|^2
=\langle R^*Rx,x\rangle
=\langle\operatorname{Im}(PR)x,x\rangle
=0.
\]

But every resolvent is injective, so `x=0`. Hence `QH={0}`, therefore `P=I`. The fixed space of `I\otimes U` is all of `H`, and thus

\[
\boxed{U=I_{\mathcal K}.}
\]

No eigenvectors, matrix trace, compactness, discrete spectrum, or finite multiplicity enter the argument. Since the prime `p` was arbitrary, every `U_p` collapses independently; no cross-prime commutativity hypothesis is needed.

The proof also shows why replacing a finite matrix by a unitary with purely continuous spectrum cannot evade the obstruction. Cesaro averaging projects exactly onto the eigenvalue-`1` subspace, while positivity of the self-adjoint resolvent forces that fixed subspace to be the whole internal fiber.

## 3. After cocycle collapse the exponent lattice becomes an inert multiplicity factor

Once all `U_p=I`, the covariance reduces to

\[
RV_p=V_pR
\qquad\forall p.
\]

Since `Dom(L)=Ran(R)`, this resolvent commutation implies

\[
V_p\operatorname{Dom}(L)\subseteq\operatorname{Dom}(L),
\qquad
LV_p=V_pL
\]

on `Dom(L)`. Self-adjointness then gives the corresponding adjoint relation. Indeed, for `x,y in Dom(L)`,

\[
\langle V_p^*x,Ly\rangle
=\langle x,V_pLy\rangle
=\langle x,LV_py\rangle
=\langle Lx,V_py\rangle
=\langle V_p^*Lx,y\rangle.
\]

Hence `V_p^*x in Dom(L)` and

\[
LV_p^*=V_p^*L.
\]

In particular `R` commutes with every `V_p^*` as well.

Let

\[
E=e_1\otimes\mathcal K.
\]

This is exactly the joint vacuum fiber

\[
E=\bigcap_p\ker V_p^*.
\]

Because `R` commutes with every `V_p^*`, it preserves `E`. Thus there is a bounded operator `A` on `K` with

\[
R(e_1\otimes\xi)=e_1\otimes A\xi.
\]

For any integer `n`, write `V_n=\prod_pV_p^{v_p(n)}`. Then

\[
\begin{aligned}
R(e_n\otimes\xi)
&=RV_n(e_1\otimes\xi)\\
&=V_nR(e_1\otimes\xi)\\
&=e_n\otimes A\xi.
\end{aligned}
\]

Therefore

\[
R=I\otimes A.
\]

The vacuum fiber reduces the self-adjoint operator `L`; writing its restriction there as `K_0=K_0^*`, equality of resolvents gives

\[
A=(K_0-i)^{-1}
\]

and consequently

\[
L=I\otimes K_0.
\]

Unlike the finite-dimensional conclusion in `PL-195`, `K_0` may now be unbounded and may have arbitrary real spectrum. That is not an escape for the prime lattice: the spectrum is programmable entirely inside `K_0` and is simply repeated over every exponent vector. No rational-prime geometry selects it.

## 4. Adversarial controls

The result is intentionally limited to **exact unitary covariance of a genuine self-adjoint resolvent**. It does not address nonunitary operator weights, nonnormal transfer/scattering operators, covariance only modulo compact or Schatten ideals, target-relative compressions such as Nyman/model spaces, or completed global constructions in which the local action is not a pure tensor `S_p\otimes U_p`.

The internal Hilbert space may be infinite dimensional and the `U_p` may have continuous spectrum. They need not commute with one another. Those were the principal open loopholes left by the proof of `PL-195`, and they are closed here.

The exact tensor form is essential. A genuinely relational prime mechanism could let the operator attached to one prime depend on other exponent coordinates, introduce loops/branching in a different carrier, couple source and target spaces, or use a relative rather than exact intertwining relation. None of those is reduced to the present one-prime mean-ergodic identity.

The theorem is universal for any one-sided isometric coordinate shift with a pure tensor unitary fiber action. It uses no prime distribution, Euler product, analytic continuation, or zeta zero information. This universality is precisely why it is a negative structural result rather than positive RH evidence.

## 5. Prior-art and novelty audit

`PL-193` and `PL-194` treat scalar phase and arbitrary scalar weights. `PL-195` treats finite-dimensional unitary fibers and explicitly leaves infinite internal multiplicity/continuous unitary spectrum outside its proof. The present theorem closes that exact-unitary boundary without changing the earlier claims.

The surrounding operator theory is classical: vector-valued unilateral shifts, operator-valued Hardy multipliers, normal/subnormal Toeplitz operators, unitary dilations, and lambda-commuting/intertwining operators all have extensive literatures. A targeted search across those topics, including recent operator-valued Toeplitz work, found adjacent classification and dilation results but no source asserting this exact self-adjoint-resolvent covariance collapse for an arbitrary unitary fiber. No general abstract novelty claim is made. The durable contribution is the exact line-specific no-go theorem and the short mean-ergodic proof above.

No `SOURCES.md` update is required: the only named external ingredient used in the derivation is the standard von Neumann mean ergodic theorem; the targeted papers inspected during the novelty audit were adjacent rather than evidentiary dependencies.

## Consequence for the research line

The exact unitary-cocycle ladder now closes without a dimension restriction:

\[
\text{scalar phase}
\subset
\text{finite unitary fiber}
\subset
\text{arbitrary unitary Hilbert fiber}
\]

all collapse at the self-adjoint-resolvent level. Infinite multiplicity can retain an arbitrary self-adjoint spectrum only by placing it in a completely inert tensor factor `K_0`, which is not arithmetic structure.

Accordingly, a live relational prime-shift mechanism must leave the class

\[
R(S_p\otimes I)=(S_p\otimes U_p)R
\]

with fixed unitary `U_p`. The remaining structurally distinct possibilities are nonunitary/nonnormal transport with a separate coercivity principle, target-relative or source-target coupling, covariance measured by a nontrivial relative ideal/determinant rather than exact equality, or a carrier whose prime actions are not independent pure-tensor directions. Merely increasing the internal unitary multiplicity, even to continuous spectrum, cannot encode a Hilbert--Polya mechanism.