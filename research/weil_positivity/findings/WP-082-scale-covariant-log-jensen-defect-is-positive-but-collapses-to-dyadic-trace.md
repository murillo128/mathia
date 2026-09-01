# WP-082 — Scale-covariant log-Jensen defect is positive but collapses to a dyadic trace

## Claim

Continue the pointed-cover geometry of `WP-073`--`WP-081`. Let

\[
H=\ell^2(\mathbb N_0),\qquad Le_k=(k+\tfrac12)e_k,
\]

and

\[
W_ne_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\qquad
\Phi_n(X):=W_n^*XW_n.
\]

Thus `Phi_n` is the unital cover compression underlying the transfer `rho_n=n Phi_n`, and `WP-074`/`WP-081` give the exact representative-level covariance

\[
\boxed{\Phi_n(L)=nL.}
\tag{1}
\]

A natural way to use this representative before passing to trace or coinvariants is the logarithmic Jensen defect. For

\[
c>-\frac12,\qquad A_c:=L+cI,
\]

define, initially entrywise on the diagonal,

\[
\boxed{
J_{n,c}:=\log\Phi_n(A_c)-\Phi_n(\log A_c).
}
\tag{2}
\]

Then:

1. for every `n>1` and every `c>-1/2`, `J_{n,c}` is a strictly positive trace-class diagonal operator;
2. its trace is exactly
   \[
   \boxed{
   \operatorname{Tr}J_{n,c}
   =-\frac cn\log n
   +\frac{1-1/n}{2}\log(2\pi)
   -\log\Gamma\!\left(\frac12+\frac cn\right)
   +\frac1n\log\Gamma\!\left(\frac12+c\right);
   }
   \tag{3}
   \]
3. at the unique fixed-shift representative with exact degree covariance, `c=0`, all nontrivial Gamma dependence cancels and
   \[
   \boxed{
   \operatorname{Tr}J_{n,0}
   =\frac{1-1/n}{2}\log 2;
   }
   \tag{4}
   \]
4. this collapse is rigid inside the whole diagonal all-degree covariant class: if a diagonal positive ladder `A=diag(a_k)` satisfies `Phi_n(A)=nA` for every `n`, then `A` is a positive scalar multiple of `L`, and the scalar cancels from its logarithmic Jensen defect;
5. the covariant defects remain a flat semigroup cocycle and their Möbius primitive has the wrong arithmetic support and normalization. In particular, for prime powers its positive primitive trace is
   \[
   \boxed{
   \operatorname{Tr}(J_{p^k,0}-J_{p^{k-1},0})
   =\frac{\log2}{2}\frac{p-1}{p^k},
   }
   \tag{5}
   \]
   not `log p`, while for general `n>1` the Möbius-primitive trace is nonzero for every prime support rather than only prime powers.

Hence the most direct nonlinear positive response that **does preserve the representative-level scale covariance left open by `WP-081`** does not produce a Riemann archimedean channel. The same block geometry that makes the logarithmic Jensen gap positive forces the covariant half-integer ladder to a bounded dyadic statistic. Gamma dependence reappears in the matched shifted controls, but precisely after exact cover covariance has been broken.

This is a negative result for the route

```text
pointed cover + exact diagonal scale covariance
+ logarithmic Jensen/compression positivity
    -> intrinsic archimedean Weil term.
```

It does **not** classify non-diagonal or matrix-valued covariant generators, genuinely coupled finite--archimedean coefficient objects, noncommutative higher cohomology, singular boundary responses, or other nonlinear positive constructions.

**Evidence status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + MATCHED-CONTROL + CLASSICAL-JENSEN/GAMMA`.

## 1. The cover compression turns the defect into an exact block Jensen gap

For a diagonal operator `X=diag(x_j)`,

\[
\Phi_n(X)e_k
=\frac1n\sum_{r=0}^{n-1}x_{nk+r}\,e_k.
\tag{6}
\]

Write

\[
a=\frac12+c>0.
\]

Since

\[
(A_c)_{jj}=j+a,
\]

we obtain

\[
\Phi_n(A_c)e_k
=\left(\frac1n\sum_{r=0}^{n-1}(nk+r+a)\right)e_k
=\left(n(k+\tfrac12)+c\right)e_k.
\tag{7}
\]

Therefore

\[
J_{n,c}e_k=j_{n,c}(k)e_k,
\]

where

\[
\boxed{
 j_{n,c}(k)
 =\log\!\left(n(k+\tfrac12)+c\right)
 -\frac1n\sum_{r=0}^{n-1}\log(nk+r+a).
}
\tag{8}
\]

The first argument of `log` is exactly the arithmetic mean of the `n` positive numbers

\[
nk+a,\ nk+1+a,\ldots,nk+n-1+a.
\]

Because `log` is strictly concave and those numbers are distinct for `n>1`, scalar Jensen gives

\[
\boxed{j_{n,c}(k)>0}
\qquad(k\ge0,n>1,c>-1/2).
\tag{9}
\]

Thus the sign is independent of zeta, zeros, RH, analytic continuation, or a fitted kernel. It is an ordinary positive Jensen gap forced by the intrinsic cover partition.

The terminology in (2) is consistent with the classical Davis--Choi--Jensen framework for compression by an isometry and operator-concave `log`. No unbounded-operator extension of that theorem is needed here: equations (6)--(9) prove positivity directly on the common finite-support core and identify the resulting bounded diagonal operator explicitly.

## 2. The positive defect is trace class and its trace is an exact Gamma endpoint expression

Set

\[
b:=\frac12+\frac cn.
\]

Equation (8) can be rewritten as

\[
j_{n,c}(k)
=\log n+\log(k+b)
-\frac1n\sum_{r=0}^{n-1}\log(nk+r+a).
\tag{10}
\]

For the first `K` diagonal entries,

\[
\begin{aligned}
T_{n,c}(K)
&:=\sum_{k=0}^{K-1}j_{n,c}(k)\\
&=K\log n
+\log\Gamma(K+b)-\log\Gamma(b)\\
&\qquad
-\frac1n\left[
\log\Gamma(nK+a)-\log\Gamma(a)
\right].
\end{aligned}
\tag{11}
\]

This uses only the Gamma recurrence to package the finite products. Applying Stirling's expansion to the two large arguments gives

\[
\lim_{K\to\infty}T_{n,c}(K)
=-\frac cn\log n
+\frac{1-1/n}{2}\log(2\pi)
-\log\Gamma(b)
+\frac1n\log\Gamma(a),
\tag{12}
\]

which is (3).

Because every summand in (11) is positive and the limit is finite, `J_{n,c}` is positive trace class. One may also read the local decay from the centered-block expansion:

\[
j_{n,c}(k)
=\frac{n^2-1}{24n^2}\frac1{k^2}
+O_{n,c}(k^{-3}).
\tag{13}
\]

The leading trace-class coefficient is independent of the shift. The finite total trace, however, retains the endpoint shift through the Gamma terms in (3).

## 3. Exact covariance forces the Gamma endpoint to collapse to `log 2`

At `c=0`,

\[
a=b=\frac12.
\]

Substituting `Gamma(1/2)=sqrt(pi)` into (3) yields

\[
\begin{aligned}
\operatorname{Tr}J_{n,0}
&=\frac{1-1/n}{2}\log(2\pi)
-(1-1/n)\log\Gamma(1/2)\\
&=\frac{1-1/n}{2}\log 2.
\end{aligned}
\tag{14}
\]

So the unique fixed-shift point selected in `WP-081` by

\[
\Phi_n(L)=nL
\]

is exactly the point at which the Gamma endpoint expression becomes the elementary bounded degree statistic

\[
n\longmapsto\frac{\log2}{2}\left(1-\frac1n\right).
\tag{15}
\]

This does **not** resemble the archimedean part of the Weil explicit formula, which is a nontrivial functional involving the completed zeta Gamma factor and the test function. Here there is no test-function variable or archimedean spectral channel left at all; ordinary trace sees only (15).

The conclusion is intentionally narrower than saying that `Gamma` cannot arise from the cover geometry. Equation (3) shows that Gamma functions do arise from the block endpoint product. The obstruction is sharper: **the exact half-integer representative-level covariance that made the branch interesting removes that dependence from this canonical positive logarithmic response.**

## 4. The collapse is rigid for every diagonal all-degree covariant ladder

The shifted family in `WP-081` establishes uniqueness only inside `L+cI`. For the present route one can enlarge the matched class substantially.

Let

\[
A=\operatorname{diag}(a_0,a_1,a_2,\ldots)
\]

be a diagonal operator whose finite-support core is preserved by every cover compression, and assume

\[
\boxed{\Phi_n(A)=nA}
\qquad\text{for every }n\ge1.
\tag{16}
\]

Taking the `k=0` diagonal entry and using (6) gives

\[
\frac1n\sum_{r=0}^{n-1}a_r=na_0,
\]

hence

\[
\sum_{r=0}^{n-1}a_r=n^2a_0.
\tag{17}
\]

Subtracting the same formula with `n-1` gives, for `n>=2`,

\[
a_{n-1}
=\bigl(n^2-(n-1)^2\bigr)a_0
=(2n-1)a_0.
\tag{18}
\]

Thus

\[
\boxed{A=2a_0L.}
\tag{19}
\]

For a positive nonzero ladder `a_0>0`. Consequently every positive diagonal all-degree covariant ladder is just a scalar multiple of `L`.

But a scalar multiple cannot change the logarithmic Jensen defect:

\[
\begin{aligned}
\log\Phi_n(\alpha L)-\Phi_n(\log(\alpha L))
&=\log(\alpha nL)-\Phi_n(\log\alpha I+\log L)\\
&=\log(nL)-\Phi_n(\log L)\\
&=J_{n,0}.
\end{aligned}
\tag{20}
\]

Therefore (14) is not an accident of a normalization choice within the diagonal covariant class. There is no alternative positive diagonal exact-covariance ladder whose logarithmic compression gap can be tuned to retain a different Gamma endpoint.

## 5. Shifted controls keep positivity but recover Gamma only by breaking covariance

For every `c>-1/2`, equation (9) shows that `J_{n,c}` remains strictly positive. Thus positivity itself does not select the Riemann half-integer origin.

On the other hand,

\[
\Phi_n(A_c)=nL+cI,
\]

whereas exact degree covariance of the shifted ladder would require

\[
nA_c=nL+ncI.
\]

For any `n>1`, these agree if and only if `c=0`. Hence the continuum of matched controls has the following exact behavior:

```text
all c > -1/2:
    positive trace-class logarithmic Jensen defect

c = 0:
    exact all-degree cover covariance
    trace = (log 2)/2 * (1 - 1/n)

c != 0:
    Gamma-dependent endpoint trace
    exact cover covariance lost
```

This is a stronger control than merely changing a regularization. The Hilbert space, block covers, multiplicative semigroup, compression map, positivity theorem, and logarithmic functional are identical; only the spectral origin is shifted.

## 6. The covariant Jensen defects are still flat under degree composition

The cover isometries satisfy

\[
W_mW_n=W_{mn},
\]

so

\[
\Phi_n\Phi_m=\Phi_{mn}.
\tag{21}
\]

For the shifted family, note that

\[
\Phi_m(A_c)=mA_{c/m}.
\]

Adding and subtracting `Phi_n(log Phi_m(A_c))` in (2) gives the exact chain rule

\[
\boxed{
J_{mn,c}=J_{n,c/m}+\Phi_n(J_{m,c}).
}
\tag{22}
\]

At the covariant point this closes on one representative:

\[
\boxed{
J_{mn,0}=J_{n,0}+\Phi_n(J_{m,0}).
}
\tag{23}
\]

Commutativity of the degree semigroup then implies

\[
(\Phi_n-I)J_{m,0}
=(\Phi_m-I)J_{n,0}.
\tag{24}
\]

Thus the direct logarithmic nonlinear response does not create a nonzero two-degree curvature either. It is another flat semigroup `1`-cocycle, now arising from the failure of `log` to commute with cover compression.

For diagonal trace-class `X`, equation (6) also gives

\[
\operatorname{Tr}\Phi_n(X)=\frac1n\operatorname{Tr}X.
\tag{25}
\]

Taking traces in (23) yields

\[
t(mn)=t(n)+\frac1n t(m),
\qquad
t(n):=\operatorname{Tr}J_{n,0},
\tag{26}
\]

which is exactly satisfied by (15). The covariant trace therefore carries a universal weighted-degree cocycle rather than the additive `log n` class of `WP-074`/`WP-081`.

Entrywise, exact covariance also gives the formal identity

\[
J_{n,0}
=\log n\,I+\log L-\Phi_n(\log L).
\tag{27}
\]

The individual terms on the right are not trace class; their cancellation is. This is another warning against interpreting the finite trace as a new independent archimedean object without the full compression relation.

## 7. Möbius primitive extraction gives the wrong arithmetic channel

To compare with the successful finite-place extraction of `WP-078`/`WP-081`, define

\[
P_n:=\sum_{d\mid n}\mu(d)J_{n/d,0}.
\tag{28}
\]

At the trace level, with

\[
\alpha:=\frac{\log2}{2},
\qquad
t(n)=\alpha(1-1/n),
\]

we obtain for `n>1`

\[
\begin{aligned}
\operatorname{Tr}P_n
&=\alpha\sum_{d\mid n}\mu(d)\left(1-\frac d n\right)\\
&=-\frac\alpha n\sum_{d\mid n}\mu(d)d\\
&=-\frac\alpha n\prod_{p\mid n}(1-p).
\end{aligned}
\tag{29}
\]

This is nonzero for every `n>1`, including integers with several distinct prime factors. It therefore does not recover Mangoldt support.

For a prime power, only `1,p` survive in the Möbius sum and (23) gives the stronger operator identity

\[
P_{p^k}
=J_{p^k,0}-J_{p^{k-1},0}
=\Phi_{p^{k-1}}(J_{p,0})\succeq0.
\tag{30}
\]

Its trace is

\[
\operatorname{Tr}P_{p^k}
=\frac1{p^{k-1}}\operatorname{Tr}J_{p,0}
=\alpha\frac{p-1}{p^k},
\tag{31}
\]

which proves (5). Combining this with the pointed-cover overlap from `WP-073`,

\[
\langle e_0,W_{p^k}e_0\rangle=p^{-k/2},
\]

would produce a scalar proportional to

\[
\frac{p-1}{p^{3k/2}},
\tag{32}
\]

not

\[
\frac{\log p}{p^{k/2}}.
\]

So this positive representative-sensitive response fails already at the finite arithmetic bridge, before one asks it to reproduce the full archimedean/polar completion.

## 8. Universality and prior-art audit

The sign mechanism is classical. Jensen's operator inequality for compressions goes back to Chandler Davis, *A Schwarz inequality for convex operator functions*, Proc. Amer. Math. Soc. **8** (1957), 42--44, DOI `10.1090/S0002-9939-1957-0084120-4`; the modern Davis--Choi--Jensen literature treats the corresponding gap functionals, including the logarithm. A direct modern anchor is S. S. Dragomir, *Operator quasilinearity of some functionals associated with Davis--Choi--Jensen's inequality for positive maps*, Bull. Aust. Math. Soc. **95** (2017), 322--332, DOI `10.1017/S0004972716000769`. The Gamma recurrence and Stirling expansion used in (11)--(12) are classical; see NIST DLMF Chapter 5, especially §5.11. No theorem-level novelty is claimed for Jensen positivity, Gamma products, or Stirling asymptotics.

The Mathia-specific result is their exact specialization to the pointed multiplicative cover system together with the rigid covariance classification (16)--(20). That specialization gives a decisive control on the route left open by `WP-081`: preserving the unique diagonal representative-level scale covariance does not make the canonical positive log-compression defect look more like the Riemann archimedean term; it makes its scalar trace **simpler**, reducing it to `log 2` times `1-1/n`.

The construction is also arithmetically universal. Equations (6)--(27) know only the integer block-cover semigroup; no primality property enters. Restricting degrees to primes after the fact cannot turn the sign theorem into rational-prime rigidity, and the Möbius test (29) makes the mismatch explicit.

This mechanism is therefore not a disguised Weil-positive functional, a Hilbert--Pólya spectrum, a Connes trace formula, or a zero-based positivity criterion. It fails earlier: its independently positive scalar response has the wrong degree law and no global test-function channel.

## 9. Exact falsification surface

The finding can be checked or killed by the following finite/exact tests:

1. verify the block-compression formula (6) from the definition of `W_n`;
2. verify the arithmetic mean identity (7) and strict Jensen positivity (9);
3. verify the finite Gamma partial trace (11) and its Stirling limit (12);
4. at `c=0`, verify the exact cancellation to (14);
5. test the diagonal covariance classification by solving `Phi_n(A)=nA` from its `k=0` entries, yielding (17)--(19);
6. verify the composition law (22) from `Phi_n Phi_m=Phi_mn`;
7. verify diagonal trace scaling (25) and the weighted cocycle law (26);
8. verify the Möbius trace formula (29) and prime-power positive identity (30).

Failure of items 1--8 invalidates the claimed obstruction. A construction based on non-diagonal covariance, a different coefficient module, a genuinely non-flat finite--archimedean interaction, or a positive response not reducible to this logarithmic block Jensen gap exits the hypotheses rather than contradicting the finding.

## Research consequence

`WP-081` showed that the positive resolvent cover cocycle and its Mangoldt prime-ray package forget the unique representative-level datum that distinguishes `L=N+1/2`; it therefore left **exact scale covariance before the positivity readout** as a live escape.

The logarithmic Jensen defect is the most direct positive nonlinear test of that escape: it uses `L` before quotienting, positivity is automatic, finite products naturally expose Gamma endpoints, and the construction is multiplicatively compatible. Yet exact covariance rigidifies the diagonal generator to `L` up to scale and forces

\[
\boxed{
\operatorname{Tr}J_{n,0}
=\frac{\log2}{2}\left(1-\frac1n\right),
}
\]

while the semigroup curvature remains zero and Möbius extraction has the wrong arithmetic support and weight.

Accordingly, the next viable cover-based route must do more than preserve the half-integer representative inside a scalar/diagonal positive compression. It must create a **genuinely coupled, non-flat finite--archimedean object before scalarization** -- for example through non-diagonal coefficient data, a matrix-valued or boundary interaction, higher cohomology with nonzero curvature, or another intrinsic structure whose sign theorem and local-to-global decomposition survive matched controls. Merely replacing the resolvent cocycle by the canonical logarithmic Jensen gap does not supply the missing global Weil positivity mechanism.
