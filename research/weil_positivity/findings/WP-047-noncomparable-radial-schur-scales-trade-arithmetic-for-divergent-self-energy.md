# WP-047 — noncomparable radial Schur scales trade arithmetic for divergent self-energy

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the non-comparable finite-radial escape left open by `WP-046`.  On every fixed finite primitive-shell space, allow the retained and eliminated Prime-Circle radial channels to approach the boundary at completely unrelated shell-dependent rates.  The corresponding positive Schur/Feshbach response has an exact leading decomposition

\[
\boxed{
\mathcal S_\varepsilon
=Q_\varepsilon+R_\varepsilon C R_\varepsilon+o(1),
}
\]

where `C` is the Prime-Circle boundary birth operator carrying the finite Weil coefficients, `Q_epsilon` is a nonnegative **diagonal radial self-energy**, and `R_epsilon` is a diagonal attenuation determined only by the relative radial boundary scales.  A finite operator-norm boundary response forces `R_epsilon -> 0`, so every cross-shell arithmetic entry disappears.  Conversely, keeping a nonzero fraction of `C` forces the corresponding diagonal entries of `Q_epsilon` to diverge.  If that divergence is subtracted, the surviving arithmetic finite part is only a diagonal congruence of `C` and therefore inherits its indefiniteness whenever the attenuation is invertible.

Thus non-comparable finite radial clocks do not evade `WP-044`--`WP-046`.  They expose a strict trilemma: keep Schur positivity and a finite limit, and arithmetic vanishes; normalize the divergent positive response, and arithmetic again vanishes; subtract the divergent self-energy to retain arithmetic, and the Schur sign theorem no longer applies, with the residual reverting to the already-indefinite birth form.  This does **not** rule out an infinite-dimensional radial/archimedean sector, a joint shell-cutoff/boundary limit, a deformation of the leading cross-shell feature geometry, or a singular renormalization with a genuinely new independent sign theorem.

## 1. Arbitrary two-channel shell-dependent boundary scales

Fix a finite primitive-shell set `S` and write

\[
E=\mathbb C^S.
\]

`WP-036` and `WP-046` give the exact positive shell-dependent radial Gram construction.  Take two radial channels and assign, for every shell `n in S`, arbitrary radii

\[
0<x_n(\varepsilon),y_n(\varepsilon)<1,
\qquad
x_n(\varepsilon),y_n(\varepsilon)\longrightarrow1
\]

as `epsilon -> 0`.  No comparability of the rates is assumed.

Let `A_epsilon` be the retained-retained block, `B_epsilon` the retained-eliminated block, and `D_epsilon` the eliminated-eliminated block of the Gram matrix.  By the shell-dependent formula of `WP-046`,

\[
A_\varepsilon(m,n)
=\widehat G_{\sqrt{x_mx_n}}(m,n),
\]

\[
B_\varepsilon(m,n)
=\widehat G_{\sqrt{x_my_n}}(m,n),
\]

and

\[
D_\varepsilon(m,n)
=\widehat G_{\sqrt{y_my_n}}(m,n).
\]

The parent block matrix

\[
\begin{pmatrix}
A_\varepsilon&B_\varepsilon\\
B_\varepsilon^*&D_\varepsilon
\end{pmatrix}
\succeq0
\]

is a genuine Gram matrix for every `epsilon`.  Since every `y_n -> 1`, the eliminated block is strictly positive and invertible for sufficiently small `epsilon` on the fixed finite shell space.  Its Schur response

\[
\boxed{
\mathcal S_\varepsilon
:=A_\varepsilon
-B_\varepsilon D_\varepsilon^{-1}B_\varepsilon^*
\succeq0
}
\tag{1}
\]

therefore inherits positivity without using RH or any arithmetic sign assumption.

The question is whether abandoning comparable boundary rates can make the finite positive limit retain the birth operator `C` that `WP-046` lost.

## 2. Boundary blocks have arbitrary diagonal divergences but the same arithmetic part

Put

\[
L(z):=-\log(1-z).
\]

For every shell `n`, define

\[
a_n:=L(x_n),
\qquad
b_n:=L(\sqrt{x_ny_n}),
\qquad
d_n:=L(y_n).
\tag{2}
\]

All three tend to `+infinity`.  The fixed-box Prime-Circle boundary expansion from `WP-034` is

\[
\widehat G_z(m,n)
=L(z)\delta_{mn}+C_{mn}+o(1)
\qquad(z\to1^-).
\tag{3}
\]

Because `S` is finite, applying (3) to the finitely many pair-dependent radii gives operator-norm remainders tending to zero.  Hence

\[
\boxed{
A_\varepsilon=D_a+C+o(1),
\qquad
B_\varepsilon=D_b+C+o(1),
\qquad
D_\varepsilon=D_d+C+o(1),
}
\tag{4}
\]

where

\[
D_a=\operatorname{diag}(a_n),
\quad
D_b=\operatorname{diag}(b_n),
\quad
D_d=\operatorname{diag}(d_n).
\]

Thus non-comparable radial speeds do something genuinely new relative to `WP-046`: there need no longer be a common scalar divergence `L_epsilon I`.  But they still do **not** alter the leading cross-shell feature geometry.  Every off-diagonal shell entry of all three blocks tends to the same arithmetic coefficient `C_mn`.

## 3. Exact Schur asymptotic: radial self-energy plus attenuated birth form

The mixed logarithmic scale is never larger than the eliminated logarithmic scale by more than a bounded constant.  Indeed, with

\[
t=1-x,
\qquad
u=1-y,
\]

one has

\[
1-\sqrt{xy}
=\frac{1-xy}{1+\sqrt{xy}}.
\]

If `M=max(t,u)`, then

\[
\boxed{
\frac M2\le1-\sqrt{xy}\le M.
}
\tag{5}
\]

Therefore

\[
\boxed{
\min(a,d)
\le b
\le\min(a,d)+\log2.
}
\tag{6}
\]

In particular `b_n/d_n` is uniformly bounded for small `epsilon`.

Let

\[
P_\varepsilon:=D_bD_d^{-1}
=\operatorname{diag}(r_n),
\qquad
r_n:=\frac{b_n}{d_n},
\tag{7}
\]

and

\[
R_\varepsilon:=I-P_\varepsilon.
\tag{8}
\]

Since `min_n d_n -> infinity`, the finite-dimensional resolvent expansion gives, entrywise and hence in operator norm after sandwiching by the blocks in (4),

\[
(D_d+C+o(1))^{-1}
=D_d^{-1}-D_d^{-1}CD_d^{-1}+	ext{higher terms},
\tag{9}
\]

where every omitted contribution to the Schur product is `o(1)`.  The potentially unequal shell scales cause no problem: each occurrence of `D_b` is paired with the same shell's `D_d^{-1}`, and (6) keeps those ratios bounded.

Substituting (9) into (1) gives

\[
\begin{aligned}
B_\varepsilon D_\varepsilon^{-1}B_\varepsilon^*
&=
D_bD_d^{-1}D_b
+P_\varepsilon C
+CP_\varepsilon
-P_\varepsilon CP_\varepsilon
+o(1).
\end{aligned}
\tag{10}
\]

Consequently

\[
\boxed{
\mathcal S_\varepsilon
=Q_\varepsilon
+R_\varepsilon C R_\varepsilon
+o(1),
}
\tag{11}
\]

with the diagonal radial self-energy

\[
\boxed{
Q_\varepsilon
:=\operatorname{diag}(q_n),
\qquad
q_n:=a_n-\frac{b_n^2}{d_n}.
}
\tag{12}
\]

Equation (11) is the main structural identity.  Non-comparable radial clocks do not generate a new cross-shell operator.  They can only attenuate the existing birth form by a diagonal congruence, while adding a positive radial self-energy.

## 4. The radial self-energy is intrinsically nonnegative

For scalar radii `x,y`, the matrix

\[
\begin{pmatrix}
L(x)&L(\sqrt{xy})\\
L(\sqrt{xy})&L(y)
\end{pmatrix}
\]

is positive semidefinite because

\[
L(\sqrt{xy})
=\sum_{r\ge1}\frac{(xy)^{r/2}}r
\]

is itself the Gram kernel of the radial feature vector

\[
\left(\frac{x^{r/2}}{\sqrt r}\right)_{r\ge1}.
\]

Therefore its Schur complement is nonnegative:

\[
\boxed{
q_n
=a_n-\frac{b_n^2}{d_n}
\ge0.
}
\tag{13}
\]

This is not a hand-chosen counterterm.  `Q_epsilon` is exactly the positive conditional radial variance left after eliminating the second channel.

Equation (11) therefore splits the positive Schur response into the only two possible leading components available inside this finite-radial geometry:

```text
universal radial conditional self-energy Q_epsilon >= 0
        +
diagonally attenuated Prime-Circle birth form R_epsilon C R_epsilon.
```

The rest of the argument shows that these two components cannot simultaneously give a finite positive boundary form carrying nonzero arithmetic coupling.

## 5. A bounded positive Schur limit forces the arithmetic attenuation to zero

The decisive scalar lemma is that bounded conditional self-energy forces the two logarithmic boundary scales to be comparable up to `O(1)`.

Let

\[
c_0:=\log2.
\]

By (6), if `a>=d`, then `d<=b<=d+c_0`, and hence

\[
q
=a-\frac{b^2}{d}
\ge
(a-d)-2c_0-\frac{c_0^2}{d}.
\tag{14}
\]

Thus bounded `q` forces `a-d=O(1)` in this case.

If `a<=d`, then `a<=b<=a+c_0`, so

\[
q
\ge
\frac{a(d-a)}d
-2c_0-rac{c_0^2}{d}.
\tag{15}
\]

If `d>=2a`, the first term is at least `a/2 -> infinity`.  Otherwise `d<2a`, so it is at least `(d-a)/2`.  Therefore bounded `q` again forces

\[
\boxed{|a-d|=O(1).}
\tag{16}
\]

Since `d -> infinity`, equations (6) and (16) imply

\[
\boxed{
r=\frac bd\longrightarrow1.}
\tag{17}
\]

Now suppose the positive matrices `S_epsilon` have a bounded operator-norm subsequence.  In (11), `R_epsilon C R_epsilon` is uniformly bounded because `C` is fixed and `R_epsilon` is bounded by (6).  Hence every `q_n` is bounded along that subsequence.  Applying (17) shell by shell gives

\[
\boxed{R_\varepsilon\longrightarrow0.}
\tag{18}
\]

Therefore

\[
\boxed{
\mathcal S_\varepsilon
=Q_\varepsilon+o(1)
}
\tag{19}
\]

along every bounded finite boundary subsequence.  In particular, for `m!=n`,

\[
\boxed{
\mathcal S_\varepsilon(m,n)\longrightarrow0.
}
\tag{20}
\]

So every finite positive Schur boundary response is shell diagonal.  The cross-shell Prime-Circle birth coefficients, including the interior Weil values

\[
C_{dp^k,d}
=-\frac{\log p}{p^{k/2}},
\]

cannot survive.

This extends `WP-046` beyond comparable shell-dependent speeds: **comparability is not an assumption needed for a finite positive limit; it is forced by finiteness itself.**

## 6. Genuinely non-comparable scales force divergent positive self-energy

The same inequalities give the converse obstruction.  If

\[
|a_n-d_n|\longrightarrow\infty
\]

on any shell, then (14)--(15) imply

\[
\boxed{q_n\longrightarrow\infty.}
\tag{21}
\]

Hence the corresponding Schur diagonal diverges positively unless one performs an additional subtraction or normalization.

A transparent matched family is

\[
1-x_n=c_n\varepsilon^{\alpha_n},
\qquad
1-y_n=d_n^{(0)}\varepsilon^{\beta_n},
\qquad
\alpha_n,\beta_n>0,
\tag{22}
\]

with fixed positive constants `c_n,d_n^(0)`.  Put

\[
L_\varepsilon=-\log\varepsilon.
\]

Then

\[
a_n=\alpha_nL_\varepsilon+O(1),
\qquad
d_n=\beta_nL_\varepsilon+O(1),
\]

and (6) gives

\[
b_n=\min(\alpha_n,\beta_n)L_\varepsilon+O(1).
\tag{23}
\]

Therefore

\[
\boxed{
r_n\longrightarrow
\frac{\min(\alpha_n,\beta_n)}{\beta_n},
}
\tag{24}
\]

while

\[
\boxed{
\frac{q_n}{L_\varepsilon}
\longrightarrow
\begin{cases}
\displaystyle
\alpha_n\frac{\beta_n-\alpha_n}{\beta_n},
&\alpha_n<\beta_n,\\[3mm]
\alpha_n-\beta_n,
&\alpha_n>\beta_n,\\[1mm]
0,&\alpha_n=\beta_n.
\end{cases}
}
\tag{25}
\]

Thus every unequal pair of power exponents produces a divergent positive self-energy.

The only case that retains a nonzero fraction of the arithmetic birth form is

\[
\alpha_n<\beta_n,
\]

for which

\[
1-r_n\longrightarrow1-\frac{\alpha_n}{\beta_n}>0.
\tag{26}
\]

But equation (25) then simultaneously gives

\[
q_n\asymp L_\varepsilon\longrightarrow\infty.
\]

This is the promised tradeoff in its simplest exact form: **nonzero arithmetic transmission requires divergent positive radial self-energy.**

## 7. The two natural repairs either erase arithmetic or restore the old indefiniteness

There are two obvious ways to handle the divergence in Section 6, and neither yields a new Weil-positive form.

### Positive normalization

For the power-law family, divide the positive Schur response by `L_epsilon`.  Equation (11) and the boundedness of `R_epsilon C R_epsilon` give

\[
\boxed{
\frac1{L_\varepsilon}\mathcal S_\varepsilon
\longrightarrow
\operatorname{diag}(\kappa_n)
\succeq0,
}
\tag{27}
\]

with `kappa_n` given by (25).  The arithmetic birth form disappears completely.  Any scalar normalization strong enough to tame an `O(L_epsilon)` self-energy has the same problem.

### Finite-part subtraction

Instead subtract the exact radial self-energy `Q_epsilon`.  If the ratios in (24) converge, then (11) gives

\[
\boxed{
\mathcal S_\varepsilon-Q_\varepsilon
\longrightarrow
R C R,
\qquad
R=\operatorname{diag}
\left(1-\frac{\min(\alpha_n,\beta_n)}{\beta_n}
\right).
}
\tag{28}
\]

This subtraction is not sign preserving; Schur positivity applies to `S_epsilon`, not to its finite part after a positive divergent diagonal has been removed.

Worse, whenever `alpha_n<beta_n` on every shell of a fixed box, `R` is invertible.  Sylvester inertia is therefore unchanged:

\[
\boxed{
\operatorname{Inertia}(RCR)
=\operatorname{Inertia}(C).
}
\tag{29}
\]

On the one-prime box

\[
\{1,p,\ldots,p^A\},
\qquad p\ge3,
\]

`WP-034` gives

\[
\operatorname{Spec}(C)
=(\log p)
\left(
\{-A\}\cup
\left\{\frac1{p-1}-j:0\le j<A\right\}
\right),
\]

so

\[
n_-(C)=A.
\]

Hence the finite arithmetic residual in (28) has the same `A` negative directions.  Allowing unequal radial exponents has not manufactured a new sign theorem; after the universal self-energy is removed, it has merely diagonally rescaled the old indefinite birth form.

This yields the finite-radial trilemma:

```text
finite positive Schur limit
    -> radial scales forced comparable
    -> R -> 0
    -> C disappears;

normalize a divergent positive Schur response
    -> Q survives
    -> C disappears;

subtract Q to retain C
    -> residual is R C R
    -> inherited Schur positivity is lost
    -> when R is invertible, the old negative inertia survives exactly.
```

## 8. Matched controls and falsification tests

The obstruction is deliberately arithmetic-blind after the Prime-Circle boundary expansion (4) is established.  Replace `C` by any fixed bounded self-adjoint matrix `H` and the same calculation yields

\[
\mathcal S_\varepsilon
=Q_\varepsilon+R_\varepsilon H R_\varepsilon+o(1).
\]

Thus the tradeoff is a structural property of a Gram family whose different radial blocks share one common finite shell operator behind unequal diagonal logarithmic divergences.  Primality enters only through the identity of `C`, not through the Schur mechanism.

Useful exact controls are:

1. **Duplicate channels:** `x_n=y_n` gives `a_n=b_n=d_n`, hence `Q=0`, `R=0`, and the Schur response vanishes, as it must for two identical Gram feature channels.
2. **Comparable linear speeds:** `1-x_n=c_n epsilon`, `1-y_n=d_n epsilon` gives `r_n->1`; expanding `q_n` recovers the universal logarithmic conditional-covariance scalar from `WP-045`/`WP-046`.
3. **Unequal power speeds:** equation (25) gives a strictly positive divergent coefficient for every `alpha_n != beta_n`.
4. **Arithmetic residual:** choose `alpha_n<beta_n` uniformly on a one-prime box.  Then `R` is invertible and (29) forces the exact negative index from `WP-034` to survive after finite-part subtraction.

The claim can be falsified by any one of the following:

- an exact expansion of the Prime-Circle two-channel Schur response contradicting (11);
- boundary radii with bounded `q_n` but `b_n/d_n` not tending to `1`;
- a bounded finite Schur boundary limit with a nonzero off-diagonal shell entry;
- a power-law family violating (24) or (25);
- an invertible diagonal `R` for which `R C R` has different inertia from `C`.

The first four would attack the Mathia-specific asymptotic; the last would contradict ordinary Hermitian congruence theory.

## 9. Prior-art and novelty boundary

Schur complements, conditional covariance, Gram positivity, Neumann resolvent expansions, and inertia under invertible congruence are standard matrix/operator theory.  A targeted prior-art audit for Schur-complement/conditional-covariance positivity and logarithmic kernels finds the expected classical machinery, not a distinct number-theoretic positivity mechanism.  No novelty is claimed for those ingredients.

The Mathia-specific content is the combination of that standard machinery with the exact Prime-Circle boundary structure

\[
\widehat G_z=L(z)I+C+o(1)
\]

and the shell-dependent polarized Gram of `WP-046`, producing the forced factorization (11) and its arithmetic/self-energy tradeoff.

This remains well short of the classical/global mechanisms already audited in `SOURCES.md`.  In particular, Connes--Consani archimedean compression changes the relevant infinite-dimensional space and pairing before the sign theorem is read off; it is not a finite radial conditional-covariance limit of this form.  Frobenius/cohomological intersection mechanisms likewise lie outside the hypotheses.  The present result should therefore be read only as a no-go for the natural finite-radial Schur escape, not as a new formulation of Weil positivity.

## 10. Consequence for the research line

`WP-036` remains the strongest same-parent finite/archimedean bridge in Prime Circle: the positive radial Mellin family contains a `psi(s/2)` channel, while its renormalized boundary finite part contains the critical prime-ray coefficients.  `WP-044`--`WP-046` showed that finite radial contrasts and comparable finite Schur couplings cannot marry those two readouts while preserving positivity.

The present result removes the remaining obvious loophole that the radial clocks merely needed to become singularly non-comparable.  On a fixed finite shell space, non-comparability can transmit a fraction of the arithmetic operator only by creating a divergent positive conditional self-energy.  Every sign-preserving finite normalization erases the arithmetic; every finite-part extraction that retains it falls back to a congruence of the already-indefinite `C`.

A surviving Mathia-native route must therefore change at least one hypothesis of (11).  The plausible boundaries are now sharper:

- deform the **leading cross-shell feature geometry** rather than only radial rates;
- use an infinite-dimensional archimedean/radial sector whose compression is not a finite Schur complement;
- couple the radial boundary limit to a cofinal shell cutoff in a geometrically forced way and prove the joint limit directly from the exact kernel;
- construct a nonlinear determinant/intersection/cohomological pairing before the collision and arithmetic pieces separate;
- or derive a singular renormalized response with a new sign theorem that does not descend merely from positivity of the unrenormalized Schur form.

Simply choosing faster or slower shell-dependent radial clocks is no longer a viable escape.
