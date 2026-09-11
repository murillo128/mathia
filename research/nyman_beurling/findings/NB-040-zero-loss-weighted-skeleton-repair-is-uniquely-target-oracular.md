# NB-040 — zero-loss weighted-skeleton repair is uniquely target-oracular

**Status:** `EXACT-DERIVED + TARGET-AUGMENTED-SHELL-QUOTIENT + ZERO-TARGET-LOSS + ONE-EXTRA-DIMENSION + N-UNIFORM-POLYNOMIAL-CONDITIONING + UNIQUE-RANK-ONE-REPAIR + NEGATIVE/ORACLE-BOUNDARY`. `NB-034` gives a source-faithful `(M-1)`-dimensional weighted skeleton with target-loss at most `1/M`, while `NB-039` proves that this loss is actually `Theta(1/M)` whenever `N>=2M`. There is an exact way to remove that loss using only one extra retained dimension: discard the maximal target-orthogonal part of the weighted tail. The resulting `M`-dimensional quotient preserves the full finite Nyman distance exactly and admits an `N`-uniform polynomially conditioned orthogonal basis. However, the unique extra retained direction is precisely the full weighted-tail target projection `P_{\widehat W_{M,N}}e`. Thus the zero-loss repair changes the representation problem but does not remove the target oracle; it isolates it into one unavoidable rank-one direction.

Use the canonical generators

\[
g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
\qquad
V_N=\operatorname{span}(g_2,\ldots,g_N),
\qquad e(x)=1,
\tag{1}
\]

and, for integers `2<=M<N`, the weighted tail of `NB-034`,

\[
\widehat h_n:=n g_n-(n+1)g_{n+1},
\qquad
\widehat W:=\widehat W_{M,N}
=\operatorname{span}(\widehat h_M,\ldots,\widehat h_{N-1}).
\tag{2}
\]

Let

\[
\widehat K:=V_N\cap\widehat W^\perp,
\qquad
\widehat k_j:=(I-P_{\widehat W})g_j\quad(2\le j\le M),
\tag{3}
\]

and write `\widehat H_{M,N}` for the Gram matrix of the basis `(\widehat k_2,\ldots,\widehat k_M)`. Define the target-orthogonal weighted tail

\[
\boxed{
\widehat W^0:=\widehat W\cap e^\perp
}
\tag{4}
\]

and its orthogonal complement inside the full finite section,

\[
\boxed{
\widehat K^0:=V_N\cap(\widehat W^0)^\perp.
}
\tag{5}
\]

Then `\widehat W^0` has codimension one in `\widehat W`,

\[
\boxed{
\dim \widehat W^0=N-M-1,
\qquad
\dim \widehat K^0=M.
}
\tag{6}
\]

More importantly, if

\[
w_{M,N}:=P_{\widehat W}e,
\qquad
L_{M,N}:=\|w_{M,N}\|^2,
\tag{7}
\]

then

\[
\boxed{
\widehat W
=\widehat W^0\oplus\operatorname{span}(w_{M,N}),
}
\tag{8}
\]

\[
\boxed{
\widehat K^0
=\widehat K\oplus\operatorname{span}(w_{M,N})
=\widehat K+\operatorname{span}(P_{V_N}e).
}
\tag{9}
\]

Consequently the target projection is preserved **exactly**:

\[
\boxed{
P_{\widehat K^0}e=P_{V_N}e,
\qquad
\operatorname{dist}(e,\widehat K^0)=d_N.
}
\tag{10}
\]

Thus the `Theta(1/M)` target-loss floor of the `(M-1)`-dimensional weighted skeleton disappears completely after adding one dimension. But that dimension is not a new source-defined arithmetic mode: it is exactly the target-selected vector `P_{\widehat W}e` which the original reduced-oracle problem did not know how to obtain.

For `N>=2M`, `NB-039` gives

\[
\boxed{
\frac{\log2}{M}
\le
L_{M,N}
=\widehat\kappa_{M,N}^2-d_N^2
\le
\frac1M.
}
\tag{11}
\]

Normalize the repair direction by

\[
\boxed{
b_{M,N}:=\frac{w_{M,N}}{L_{M,N}}.
}
\tag{12}
\]

Then

\[
\langle e,b_{M,N}\rangle=1,
\qquad
\|b_{M,N}\|^2=L_{M,N}^{-1},
\tag{13}
\]

and `b_{M,N}` is orthogonal to every `\widehat k_j`. Hence

\[
\boxed{
(\widehat k_2,\ldots,\widehat k_M,b_{M,N})
}
\tag{14}
\]

is an orthogonal-block basis of the zero-loss skeleton with Gram matrix

\[
\boxed{
H^0_{M,N}
=
\begin{pmatrix}
\widehat H_{M,N}&0\\
0&L_{M,N}^{-1}
\end{pmatrix}.
}
\tag{15}
\]

Combining (11) with the `NB-034` bounds

\[
\lambda_{\min}(\widehat H_{M,N})
\ge \frac1{14M^2H_M^2},
\qquad
\lambda_{\max}(\widehat H_{M,N})
\le2(H_M-1),
\tag{16}
\]

gives the `N`-uniform estimate

\[
\boxed{
\operatorname{cond}_2(H^0_{M,N})
\le
14M^2H_M^2
\max\left\{2(H_M-1),\frac{M}{\log2}\right\}
=O(M^3(\log M)^2).
}
\tag{17}
\]

So exact target preservation and polynomial conditioning are simultaneously possible at retained dimension `M`. The obstruction left by `NB-036`--`NB-039` is therefore not dimensionality or abstract conditioning. It is source access to the one target-selected direction in (12).

## 1. The target functional is nonzero on the weighted tail

The target pairing with a canonical generator is elementary and exact. Writing `rho(u)={u}` and substituting `u=1/x`,

\[
\begin{aligned}
\langle e,g_n\rangle
&=\int_0^1\rho\!\left(\frac1{nx}\right)dx
-\frac1n\int_0^1\rho\!\left(\frac1x\right)dx\\
&=\frac1n\int_{1/n}^{\infty}\frac{\rho(u)}{u^2}\,du
-\frac1n\int_1^{\infty}\frac{\rho(u)}{u^2}\,du\\
&=\frac1n\int_{1/n}^{1}\frac{du}{u}
=\frac{\log n}{n}.
\end{aligned}
\tag{18}
\]

Therefore

\[
\boxed{
\langle e,\widehat h_n\rangle
=\log n-\log(n+1)
=-\delta_n,
\qquad
\delta_n:=\log\frac{n+1}{n}>0.
}
\tag{19}
\]

The weighted edges are linearly independent, so `dim \widehat W=N-M`. Equation (19) shows that the target functional does not vanish on `\widehat W`; hence its kernel there has dimension `N-M-1`, proving the first part of (6).

There is also a completely explicit target-orthogonal generating family. For `M<=n<=N-2`, set

\[
\boxed{
\widetilde h_n
:=\delta_{n+1}\widehat h_n
-\delta_n\widehat h_{n+1}.
}
\tag{20}
\]

Then `\langle e,\widetilde h_n\rangle=0`. The coefficient vectors in the independent edge basis form a path family

\[
\delta_{n+1}e_n-\delta_ne_{n+1},
\]

which is itself linearly independent. There are exactly `N-M-1` such vectors, therefore

\[
\boxed{
\widehat W^0
=\operatorname{span}(\widetilde h_M,\ldots,\widetilde h_{N-2}).
}
\tag{21}
\]

For `N=M+1`, the right side is the empty span and `\widehat W^0={0}`, as it should be. Thus the **discarded** zero-target-loss sector is source/target explicit; no projection oracle is needed merely to write its generators.

## 2. The unique retained repair direction is the weighted-tail target projection

Let `w=P_{\widehat W}e`. For every `u in \widehat W^0`,

\[
\langle w,u\rangle
=\langle e,u\rangle
=0.
\tag{22}
\]

Because `w` belongs to `\widehat W` and is nonzero, dimension counting gives (8). Since `V_N=\widehat W\oplus\widehat K`, equations (8)--(9) follow.

The same statement can be expressed through the early-shell observation space of `NB-034`,

\[
E_M:=\operatorname{span}\{\mathbf1_{I_t}:1\le t<M\}.
\tag{23}
\]

That finding proves

\[
\widehat W=V_N\cap E_M^\perp.
\tag{24}
\]

Therefore

\[
\widehat W^0
=V_N\cap(E_M+\operatorname{span}e)^\perp,
\tag{25}
\]

and hence

\[
\boxed{
\widehat K^0
=P_{V_N}(E_M+\operatorname{span}e).
}
\tag{26}
\]

The old retained skeleton is `P_{V_N}E_M`; the one additional observation is literally the target functional, whose Riesz representer after projection to `V_N` is `P_{V_N}e`. This is the precise sense in which the repair is target-oracular.

Equation (10) is now immediate: `P_{V_N}e` itself lies in `\widehat K^0`, while `\widehat K^0 subset V_N`, so the best approximation to `e` from `\widehat K^0` is already the full best approximation from `V_N`.

There is also a uniqueness statement. Let `U subset \widehat W` have dimension `N-M-1`, and put

\[
K_U:=V_N\cap U^\perp.
\tag{27}
\]

The orthogonal splitting `V_N=U\oplus K_U` gives

\[
\boxed{
\operatorname{dist}(e,K_U)^2
=d_N^2+\|P_Ue\|^2.
}
\tag{28}
\]

Thus `K_U` preserves `d_N` exactly if and only if `U perp e`. But the unique codimension-one subspace of `\widehat W` contained in `e^perp` is `\widehat W^0`. Hence

\[
\boxed{
\operatorname{dist}(e,K_U)=d_N
\iff
U=\widehat W^0.
}
\tag{29}
\]

Among all repairs that discard all but one weighted-tail direction, the zero-loss repair is therefore unique, and the one retained weighted-tail line is necessarily `span(P_{\widehat W}e)`.

## 3. The quotient has one explicit extra logarithmic tail coordinate

The target-orthogonal tail also has a source-coordinate normal form. For a canonical coefficient vector

\[
v=\sum_{n=2}^Na_ng_n,
\tag{30}
\]

retain the `NB-034` weighted endpoint coordinate

\[
\tau_{M,N}(a):=M\sum_{n=M}^N\frac{a_n}{n}
\tag{31}
\]

and define one additional logarithmic tail moment

\[
\boxed{
\sigma_{M,N}(a)
:=\sum_{n=M}^N\frac{a_n}{n}\log\frac nM.
}
\tag{32}
\]

Using (18),

\[
\boxed{
\langle e,v\rangle
=
\sum_{n=2}^{M-1}\frac{a_n\log n}{n}
+\frac{\log M}{M}\tau_{M,N}(a)
+\sigma_{M,N}(a).
}
\tag{33}
\]

`NB-034` proves that the kernel of the coordinates

\[
(a_2,\ldots,a_{M-1},\tau_{M,N})
\tag{34}
\]

is exactly `\widehat W`. On that kernel, (33) reduces to

\[
\langle e,v\rangle=\sigma_{M,N}(a).
\tag{35}
\]

Consequently

\[
\boxed{
\ker\bigl(a_2,\ldots,a_{M-1},\tau_{M,N},\sigma_{M,N}\bigr)
=\widehat W^0.
}
\tag{36}
\]

Thus adding one logarithmic tail moment gives an entirely explicit algebraic coordinate system for the target-augmented quotient `V_N/\widehat W^0`. This is the coefficient-side counterpart of the geometric rank-one repair.

For the canonical best approximant

\[
p_N=P_{V_N}e=\sum_{n=2}^Na_{N,n}g_n,
\tag{37}
\]

orthogonality of the residual gives

\[
\langle e,p_N\rangle=\|p_N\|^2=1-d_N^2.
\tag{38}
\]

Therefore the additional quotient coordinate satisfies the exact identity

\[
\boxed{
\sigma_{M,N}(a_N)
=1-d_N^2
-
\sum_{n=2}^{M-1}\frac{a_{N,n}\log n}{n}
-
\frac{\log M}{M}\tau_{M,N}.
}
\tag{39}
\]

This is not a new upper bound for `d_N`; it is the oracle boundary in coefficient form. The head coordinates are Möbius-locked by `NB-020`/`NB-036`, and the weighted endpoint is uniformly Möbius-locked by `NB-035`, but exact zero-loss compression requires one additional logarithmic tail coordinate whose optimal value contains the full finite target distance. Treating (39) as if `sigma` were independently known would simply insert the desired answer into the reduced problem.

## 4. Polynomial conditioning survives, but only in the target-selected basis

Since `w in \widehat W` and `\widehat K perp \widehat W`, the basis (14) is block orthogonal. Equation (11) implies

\[
M\le\|b_{M,N}\|^2\le\frac{M}{\log2}.
\tag{40}
\]

Together with the `N`-uniform bounds (16), this proves (17). In particular, the extra target direction does **not** introduce an exponential or `N`-dependent condition number. The exact target problem can be compressed to dimension `M` while keeping polynomial conditioning in `M`.

This does not contradict the accepted target-data clue. The conditioned basis itself contains

\[
b_{M,N}
=\frac{P_{\widehat W}e}{\|P_{\widehat W}e\|^2},
\tag{41}
\]

so forming its final column requires the weighted-tail target projection. Equivalently, (26) says that the target observation contributes the Riesz representer `P_{V_N}e`, the full finite best approximant. The metric is benign **after** the missing target information has been supplied.

The result therefore separates three gates sharply:

- representation dimension: `M` is enough for exact preservation;
- abstract conditioning: `O(M^3(log M)^2)` is enough uniformly in `N`;
- source access: the unique added direction is the unresolved target projection.

The first two gates are not the obstruction for this repair. The third is.

## 5. Prior-art and adversarial boundary

The Hilbert-space facts behind (8)--(10), (28), and the block Gram matrix are elementary projection geometry; no novelty is claimed for codimension-one target orthogonalization in the abstract. The line-local content is the exact specialization to the source-defined weighted tail, the explicit local generators (20)--(21), the logarithmic quotient coordinate (32), and the use of the sharp `NB-039` loss floor to show that the unique repair direction has polynomial but non-negligible scale.

A targeted literature search over Nyman--Beurling finite sections, orthogonal complements, quotient/projection constructions, and finite target-aware Gram reductions did not locate this particular weighted-tail target-orthogonal quotient or the normal form (32)--(39). Search absence is not a priority claim. The only external mathematical inputs used here are the canonical Nyman framework already anchored in `SOURCES.md`; all quantitative statements are finite consequences of `NB-034` and `NB-039`. No source-list update is required.

Several boundaries are essential. First, exact distance preservation does not give a new estimate for `d_N`, prove `d_N->0`, or imply RH. Second, although `\widehat W^0` itself has the explicit generators (20), constructing the orthogonal retained skeleton still requires projecting against a section of dimension `N-M-1`; no reduced algorithm follows from dimension counting. Third, the polynomial bound (17) applies to the target-selected basis containing (41); it must not be advertised as a source-constructible conditioned basis. Fourth, the sharp quantitative bounds (11), (17), and (40) use `N>=2M`; the algebraic zero-loss and uniqueness statements only need `2<=M<N`. Finally, (39) is an identity for the actual optimal coefficients, not an independent arithmetic estimate for the logarithmic tail moment.

The accepted clue `CLUE-weighted-skeleton-target-data-without-full-section-oracle` therefore remains open, but its boundary is narrower. One extra target-aware quotient coordinate is enough to achieve **both exact target preservation and polynomial conditioning**. Any further progress must obtain that coordinate/direction from arithmetic information more cheaply than reconstructing `P_{V_N}e`, or avoid this unique rank-one repair altogether through a genuinely different one-sided certificate.