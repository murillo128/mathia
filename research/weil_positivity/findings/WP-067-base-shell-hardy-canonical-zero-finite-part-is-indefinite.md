# WP-067 — canonical zero-finite-part subtraction of the base-shell Hardy Gram is indefinite; finite shifts reduce to Riesz boundedness

**Status:** `EXACT-DERIVED` + `SUBSTANTIVE-CORRECTION` + `DECISIVE-BOUNDARY` + `CLASSICAL-FUNCTIONAL-ANALYSIS`. The Prime-Circle identities used below are already established in PC-075/PC-080. The renormalization dichotomy is an elementary consequence of Hilbert-space completion and the Riesz representation theorem. No theorem-level historical novelty is claimed.

The canonical Hardy/Hilbert coupling does contain a genuinely positive quadratic form whose polarization against the Prime-Circle base shell recovers the von Mangoldt function exactly. The tempting obstruction is that the formal base-shell anchor is the identity, whose norm in that positive geometry diverges. That observation is real but, by itself, it is not enough to prove that every finite renormalization preserving the same Mangoldt cross term must lose positivity.

What can be proved exactly is sharper and narrower.

Let

\[
H=\left(\frac1{j+k+1}\right)_{j,k\ge0},
\qquad
\Gamma_1=-H,
\qquad
(\Gamma_n)_{jk}=-\frac{c_n(j+k+1)}{j+k+1}\quad(n>1),
\]

and let

\[
\mathcal A_0=\operatorname{span}\{\Gamma_n:n>1\}.
\]

Define

\[
\langle A,B\rangle_H:=\operatorname{Tr}(A^*HB),
\qquad
Q_H(B):=\langle B,B\rangle_H
=\|H^{1/2}B\|_{\mathcal S_2}^2.
\]

PC-080 gives the exact mixed trace

\[
\operatorname{Tr}(\Gamma_1\Gamma_n)=-\Lambda(n),
\]

hence

\[
\boxed{L(\Gamma_n):=\operatorname{Tr}(H\Gamma_n)=\Lambda(n).}
\]

Thus the positive Hardy Gram geometry has the correct finite arithmetic polarization. However, the canonical cutoff square

\[
E_N(B):=Q_H(P_N-B)\ge0
\]

has divergent base self-energy

\[
E_N:=Q_H(P_N)=\operatorname{Tr}(P_NHP_N)
=\sum_{j=0}^{N-1}\frac1{2j+1}
=\frac12\log N+\log2+\frac\gamma2+O(N^{-2}),
\]

while its cross term converges to `L(B)`. Subtracting exactly that divergent self-energy therefore produces the canonical zero-finite-part limit

\[
\boxed{R_0(B)=Q_H(B)-2\operatorname{Re}L(B),}
\]

and this form is necessarily indefinite because `L` is nonzero.

The stronger question — whether *every* finite scalar renormalization preserving the same exact Mangoldt cross term is indefinite — is equivalent to a separate boundedness problem for `L` in the `Q_H` norm. If `L` is bounded on the Hilbert completion of `\mathcal A_0`, a finite additive constant can restore positivity; if `L` is unbounded, no finite constant can. The identity anchor being nonnormalizable does not decide between those two cases.

## 1. The base-shell cross term is exactly von Mangoldt

PC-075 constructs the canonical Hardy shell operators

\[
(\Gamma_n)_{jk}=-\frac{c_n(j+k+1)}{j+k+1}.
\]

For distinct shell labels, PC-080 proves

\[
\Gamma_m\Gamma_n\in\mathcal S_1
\]

and evaluates the mixed trace as the negative logarithm of the cyclotomic resultant. At the base shell,

\[
\Gamma_1=-H,
\]

so for every `n>1`,

\[
\operatorname{Tr}(\Gamma_1\Gamma_n)=-\Lambda(n).
\]

Therefore

\[
\boxed{\operatorname{Tr}(H\Gamma_n)=\Lambda(n).}
\]

For a finite shell combination

\[
B=\sum_{n>1}b_n\Gamma_n,
\]

put

\[
\boxed{L(B)=\operatorname{Tr}(HB)=\sum_{n>1}b_n\Lambda(n).}
\]

No zeta zero, analytic continuation, or hand-picked prime-power projector is used in this identity: it is the intrinsic base-shell resultant pairing.

## 2. The Hardy Gram form is positive on the shell span

For `A,B in \mathcal A_0`, define

\[
\langle A,B\rangle_H=\operatorname{Tr}(A^*HB).
\]

The products are trace class because `HB=-\Gamma_1B` is a finite linear combination of distinct-shell products from PC-080, and multiplication by a bounded shell operator preserves `\mathcal S_1`. Moreover,

\[
Q_H(B)=\operatorname{Tr}(B^*HB)
=\|H^{1/2}B\|_{\mathcal S_2}^2\ge0.
\]

Since the Hilbert matrix `H` is positive and injective, `Q_H(B)=0` forces `B=0`. Hence `Q_H` is a genuine positive-definite quadratic form on `\mathcal A_0`.

The arithmetic functional is its formal polarization against the identity:

\[
L(B)=\operatorname{Tr}(HB)
=\langle I,B\rangle_H,
\]

but `I` is not a vector of finite `Q_H` norm because

\[
\|I\|_H^2=\operatorname{Tr}H=\infty.
\]

This is the precise nonnormalizable-anchor statement.

## 3. Canonical cutoffs preserve the Mangoldt cross term but have divergent self-energy

Let `P_N` denote projection onto the first `N` Hardy basis vectors. Then

\[
E_N:=Q_H(P_N)
=\operatorname{Tr}(P_NHP_N)
=\sum_{j=0}^{N-1}\frac1{2j+1}.
\]

The harmonic-number expansion gives

\[
\boxed{
E_N=\frac12\log N+\log2+\frac\gamma2+O(N^{-2}).
}
\]

For fixed `B in \mathcal A_0`, `HB` is trace class, so strong convergence `P_N\to I` implies

\[
\boxed{
\operatorname{Tr}(P_NHB)\longrightarrow\operatorname{Tr}(HB)=L(B).
}
\]

Thus the unnormalized cutoff retains the exact arithmetic polarization while its norm diverges. Conversely, the normalized anchor

\[
a_N=\frac{P_N}{\sqrt{E_N}},
\qquad
Q_H(a_N)=1,
\]

satisfies

\[
\langle a_N,B\rangle_H
=\frac{\operatorname{Tr}(P_NHB)}{\sqrt{E_N}}
\longrightarrow0.
\]

So unit normalization erases the fixed shellwise Mangoldt coupling.

## 4. The canonical zero-finite-part subtraction is necessarily indefinite

For every finite `N`, positivity gives

\[
E_N(B):=Q_H(P_N-B)
=E_N-2\operatorname{Re}\operatorname{Tr}(P_NHB)+Q_H(B)
\ge0.
\]

Subtract only the divergent anchor self-energy `E_N`. For fixed `B`,

\[
E_N(B)-E_N
\longrightarrow
\boxed{R_0(B)=Q_H(B)-2\operatorname{Re}L(B).}
\]

Because `L` is nonzero, choose `B` with `L(B)\neq0` and multiply `B` by a phase so that `L(B)>0`. Along the real ray `tB`,

\[
R_0(tB)=t^2Q_H(B)-2tL(B).
\]

Its minimum occurs at

\[
t=\frac{L(B)}{Q_H(B)}
\]

and equals

\[
\boxed{
\inf_t R_0(tB)
=-\frac{|L(B)|^2}{Q_H(B)}<0.
}
\]

In particular, for a prime-power shell `m=p^k`, one may take `B=\Gamma_m`, for which `L(B)=\log p`.

Therefore the **canonical normalization with zero finite scalar part is not positive**. This conclusion uses only the exact positive square and its forced divergent self-energy.

## 5. Arbitrary finite scalar shifts are classified exactly by Riesz boundedness

The preceding calculation does **not** classify all finite renormalizations. For a real constant `c`, consider

\[
\boxed{R_c(B)=Q_H(B)-2\operatorname{Re}L(B)+c.}
\]

Equivalently this is the limit obtained from

\[
E_N(B)-E_N+c.
\]

Let `\mathcal H_{\rm shell}` be the Hilbert completion of `\mathcal A_0` in the norm

\[
\|B\|_H^2=Q_H(B).
\]

There are exactly two possibilities.

### Bounded case

If `L` is bounded in this norm, the Riesz representation theorem gives a unique

\[
g\in\mathcal H_{\rm shell}
\]

such that

\[
L(B)=\langle g,B\rangle_H.
\]

Then

\[
\boxed{
R_c(B)=\|B-g\|_H^2+c-\|g\|_H^2.
}
\]

Consequently

\[
\boxed{
R_c\ge0\text{ on }\mathcal H_{\rm shell}
\iff
c\ge\|g\|_H^2
=\|L\|^2.
}
\]

So a finite scalar renormalization *can* restore positivity if the Mangoldt functional is bounded.

### Unbounded case

If `L` is unbounded, then

\[
\sup_{B\neq0}\frac{|L(B)|^2}{Q_H(B)}=\infty.
\]

For each nonzero `B`, minimizing `R_c(tB)` over the phase and magnitude of `t` gives

\[
\inf_tR_c(tB)
=c-\frac{|L(B)|^2}{Q_H(B)}.
\]

Hence

\[
\boxed{
\inf_{B\in\mathcal A_0}R_c(B)=-\infty
\quad\text{for every finite }c.
}
\]

Thus **all finite scalar repairs fail if and only if `L` is unbounded in the Hardy-Gram shell norm**.

The exact discriminant is therefore

\[
\boxed{
\sup_{0\neq B\in\mathcal A_0}
\frac{|\operatorname{Tr}(HB)|^2}
{\operatorname{Tr}(B^*HB)}
\;\begin{cases}
<\infty,&\text{finite scalar repair exists},\\
=\infty,&\text{no finite scalar repair exists}.
\end{cases}}
\]

This boundedness question is not decided by the present derivation.

## 6. Why the divergent identity anchor does not settle the boundedness question

The formal identity satisfies

\[
L(B)=\langle I,B\rangle_H
\]

but

\[
\|I\|_H=\infty.
\]

That proves only that the **particular ambient identity anchor** is not a normalizable vector. It does not rule out the possibility that the restriction of `L` to the shell closure has a different Riesz representative `g`.

This distinction is essential because `\mathcal H_{\rm shell}` is a proper completion of the shell span in the weighted Hilbert-Schmidt geometry. A functional can be unbounded on a larger formal ambient class while remaining bounded on a restricted closed subspace. Therefore no universal no-go may be inferred from `\operatorname{Tr}H=\infty` alone.

## 7. Relation to the global Weil-positivity objective

Even the bounded branch of the dichotomy would not solve the line's main problem. A repaired form

\[
\|B-g\|_H^2
\]

would still provide only a positive shell-space completion of the exact finite Mangoldt polarization. Nothing here intrinsically generates

- the archimedean `Gamma` contribution;
- the polar/global counterterms;
- the Weil autocorrelation pairing on test functions;
- or an independent geometric bridge identifying this shell norm with the full explicit-formula quadratic form.

Accordingly, the result is a boundary classification, not an RH mechanism. It prevents the base-shell Hardy branch from claiming a stronger renormalization obstruction than has actually been proved, while preserving the exact positive geometry and exact `Lambda` polarization that make the branch worth testing.

## 8. Prior-art and novelty audit

The mathematical ingredients are classical or already persisted internally.

1. PC-075 supplies the canonical cyclotomic Hardy/Hankel operators and the universal Hilbert base channel.
2. PC-080 proves the trace-class cross-shell product and the exact identity `Tr(Gamma_1 Gamma_n)=-Lambda(n)` through the classical cyclotomic resultant.
3. Positivity of `Q_H`, Hilbert completion, bounded linear functionals, and the Riesz representation theorem are standard Hilbert-space functional analysis.
4. Subtracting a divergent self-energy and then allowing a finite scalar counterterm is standard renormalization bookkeeping; no novelty is claimed for that abstract maneuver.

The durable contribution is the exact classification **inside this Mathia-native candidate**: the canonical zero-finite-part subtraction is definitely indefinite, while the stronger all-finite-counterterm obstruction is equivalent to one concrete operator-theoretic boundedness problem and remains open.

## 9. Falsification surface

The result has five direct tests.

1. PC-080 must give `Tr(H Gamma_n)=Lambda(n)` with the stated sign.
2. `Q_H(B)=Tr(B^*HB)` must be finite and positive definite on finite shell combinations.
3. `E_N=Tr(P_NHP_N)` must have the stated `\tfrac12\log N` divergence, while `Tr(P_NHB)->L(B)` for fixed shell combinations.
4. Minimizing `Q_H(tB)-2 Re L(tB)` must give `-|L(B)|^2/Q_H(B)`.
5. For general finite `c`, Riesz completion must yield exactly the bounded/unbounded dichotomy above.

Failure of any item invalidates the corresponding conclusion. No numerical approximation, zeta-zero data, or analytic continuation is used.

## Research consequence

The base-shell Hardy Gram route now has a precise next theorem rather than a rhetorical trilemma:

\[
\boxed{
\text{decide whether }
L(B)=\operatorname{Tr}(HB)
\text{ is bounded on }
\overline{\operatorname{span}\{\Gamma_n:n>1\}}^{\,Q_H}.
}
\]

If it is unbounded, every finite scalar renormalization preserving the exact Mangoldt cross term is unbounded below. If it is bounded, the Riesz representer supplies a positive shifted square, and the research question becomes whether that representer is geometrically canonical and whether any coupled archimedean/global structure can turn the shell-space positivity into a genuine Weil form. Until that boundedness question is settled, only the canonical zero-finite-part no-go is established.