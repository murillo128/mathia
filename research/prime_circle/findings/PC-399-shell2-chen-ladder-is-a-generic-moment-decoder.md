# PC-399 — the shell-2 Chen ladder is a generic moment decoder, not a zeta selector

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for interpreting infinite Chen depth or signature injectivity by itself as new arithmetic structure, and `DECISIVE-BOUNDARY` for source-forced nonperturbative readouts beyond the signature data.

PC-347 proves that every fixed-depth ordered radial coefficient is a cyclotomic hyperlogarithmic period, while leaving genuinely infinite-depth/nonnilpotent path ordering outside its finite classification. The first question at that boundary is therefore whether passing to all depths creates a new arithmetic carrier, or merely makes the original radial shell profile recoverable.

A very small one-sided subfamily of the full Chen signature already answers this exactly. For `n>1`, put

\[
X_n(z)=\log\Phi_n(z),\qquad \omega_n=dX_n,\qquad 0\le z\le1,
\tag{1}
\]

as in PC-347, and use shell `2` as the repeated reference letter. Since

\[
X_2(z)=\log(1+z)
\tag{2}
\]

is a strictly increasing homeomorphism from `[0,1]` to `[0,\log2]`, define for `k\ge0`

\[
J_{2^k,n}
:=
J_{\underbrace{2,\ldots,2}_{k\text{ copies}},n}.
\tag{3}
\]

Then

\[
\boxed{
 k!\,J_{2^k,n}
 =
 \int_0^1 X_2(z)^k\,dX_n(z).
}
\tag{4}
\]

Consequently the infinite ladder `(J_{2^k,n})_{k\ge0}` is exactly the compact moment sequence of the finite signed measure

\[
\mu_n:=(X_2)_*(dX_n)
\quad\text{on}\quad [0,\log2].
\tag{5}
\]

Compact moment determinacy now implies that this ladder reconstructs `\mu_n`, hence reconstructs `dX_n`, hence `X_n` and `\Phi_n` themselves. In particular,

\[
\boxed{
(J_{2^k,m})_{k\ge0}=(J_{2^k,n})_{k\ge0}
\quad\Longrightarrow\quad
m=n.
}
\tag{6}
\]

Thus infinite radial order really does retain all shell information — but for the strongest possible classical reason: the repeated shell-2 coordinate acts as a compact moment parameter. The same argument works for an arbitrary finite-variation profile in place of a cyclotomic shell. Signature injectivity here is therefore a **generic decoder property**, not a prime-specific spectral mechanism.

## 1. Exact reduction of the one-sided Chen ladder to moments

For `k\ge1`, condition the simplex defining (3) on its last coordinate `z`:

\[
J_{2^k,n}
=
\int_0^1
\left(
\int_{0<z_1<\cdots<z_k<z}
\prod_{j=1}^k dX_2(z_j)
\right)
dX_n(z).
\tag{7}
\]

Because all first `k` letters are the same exact one-form,

\[
\int_{0<z_1<\cdots<z_k<z}
\prod_{j=1}^k dX_2(z_j)
=
\frac{X_2(z)^k}{k!},
\tag{8}
\]

using `X_2(0)=0`. Equations (7)--(8) prove (4). The case `k=0` gives

\[
J_n=\int_0^1dX_n=X_n(1)=\Lambda(n),
\tag{9}
\]

so the common-vertex von Mangoldt selector is precisely the **zeroth moment** of this larger ordered family.

No asymptotics, Mellin continuation, representation choice, or matrix model enters (4). It is an identity inside the intrinsic radial Chen hierarchy already defined by PC-347.

## 2. Compact moments reconstruct the entire cyclotomic radial profile

For every `n>1`, `\Phi_n` has no zero on `[0,1]`, so `X_n` is smooth there and `dX_n` is a finite signed measure. Since `X_2` is a homeomorphism, pushing forward by `X_2` loses no measure-theoretic information.

Suppose two shells `m,n>1` have the same ladder. By (4),

\[
\int_0^{\log2} t^k\,d\mu_m(t)
=
\int_0^{\log2} t^k\,d\mu_n(t)
\qquad(k=0,1,2,\ldots).
\tag{10}
\]

Polynomials are uniformly dense in `C([0,\log2])`. Hence the finite signed measure `\mu_m-\mu_n` annihilates every continuous test function and is zero. Because `X_2` is bijective,

\[
dX_m=dX_n.
\tag{11}
\]

Both potentials vanish at the origin, so `X_m=X_n` on `[0,1]`. Exponentiating gives `\Phi_m=\Phi_n` on an interval, hence as polynomials; distinct cyclotomic polynomials have distinct indices. This proves (6).

The argument is stronger than full-signature uniqueness is needed for this special path. It uses only the words consisting of repeated `2` followed by one target shell `n`; all other word orders and all other reference shells may be discarded.

## 3. Infinite depth necessarily fills the Mangoldt nullspace

Equation (9) explains why depth one is arithmetically sharp: if `n` is not a prime power, then

\[
J_n=\Lambda(n)=0.
\tag{12}
\]

But for every `n>1`, `dX_n` is not the zero measure. Therefore `\mu_n\ne0`. If a non-prime-power shell also satisfied

\[
J_{2^k,n}=0
\qquad\text{for every }k\ge1,
\tag{13}
\]

then all moments of `\mu_n` including the zeroth would vanish, forcing `\mu_n=0`, a contradiction. Hence

\[
\boxed{
\Lambda(n)=0
\quad\Longrightarrow\quad
J_{2^k,n}\ne0
\text{ for at least one }k\ge1.
}
\tag{14}
\]

So taking the complete ordered ladder cannot preserve the exact prime-power support that made the common-anchor scalar identity interesting. The extra depth does not sharpen the Mangoldt selector; it deliberately restores information that the selector had discarded.

This is not a defect of the construction. It identifies what the infinite signature is doing: it is an information-complete encoding rather than a selective arithmetic quotient.

## 4. The whole ladder is an ordinary compact Laplace transform

The exponential generating object of the ladder is particularly transparent. Since (4) already contains the factorial denominator,

\[
\begin{aligned}
G_n(w)
&:=\sum_{k=0}^{\infty}J_{2^k,n}w^k\\
&=\int_0^1 e^{wX_2(z)}\,dX_n(z)\\
&=\boxed{\int_0^1(1+z)^w\,d\log\Phi_n(z)}.
\end{aligned}
\tag{15}
\]

Equivalently,

\[
G_n(w)=\int_0^{\log2}e^{wt}\,d\mu_n(t).
\tag{16}
\]

Thus `G_n` is the bilateral Laplace transform of a finite signed measure with compact support. It is entire and obeys the elementary exponential-type bound

\[
|G_n(w)|
\le
\|\mu_n\|_{\rm TV}\,e^{(\log2)\max(\Re w,0)}.
\tag{17}
\]

Its value at `w=0` is `\Lambda(n)`, but its remaining analytic structure is the ordinary transform of the full shell profile. No functional equation, gamma factor, distinguished half-line, or critical-line symmetry is forced by (15). Any such structure would have to come from an additional cross-shell operation or source-forced readout, not from the existence or injectivity of the infinite ladder itself.

## 5. Matched control: the decoder is completely non-arithmetic

The exact same mechanism works with no roots of unity at all. Fix the reference coordinate

\[
t(z)=\log(1+z),
\tag{18}
\]

and let `Y` be any real bounded-variation profile on `[0,1]` with `Y(0)=0`. Define

\[
I_k(Y)=\frac1{k!}\int_0^1t(z)^k\,dY(z).
\tag{19}
\]

Then `(I_k(Y))_{k\ge0}` determines the pushforward `t_*(dY)` by compact moment determinacy; since `t` is a homeomorphism, it determines `dY` and hence `Y`.

Therefore a matched non-arithmetic family of profiles has exactly the same infinite-depth information-completeness. The cyclotomic input chooses a special set of profiles `Y=X_n`, but the injectivity mechanism itself does not distinguish prime powers, primes, composite conductors, or even arithmetic functions.

This matched control kills the interpretation

\[
\text{all Chen depths retain the shell}
\quad\Longrightarrow\quad
\text{new arithmetic/spectral carrier}.
\tag{20}
\]

The implication is false: retention is already guaranteed by generic compact moment inversion.

## 6. Prior art and novelty audit

The ambient uniqueness phenomenon is classical. Ben Hambly and Terry Lyons, **Uniqueness for the signature of a path of bounded variation and the reduced path group**, *Annals of Mathematics* 171:1 (2010), 109--167, DOI `10.4007/annals.2010.171.109`, proves that the full bounded-variation signature determines a path up to tree-like equivalence, extending Chen's uniqueness theory. Jiawei Chang, Nick Duffield, Hao Ni and Weijun Xu, **Signature inversion for monotone paths**, *Electronic Communications in Probability* 22 (2017), no. 42, 1--11, DOI `10.1214/17-ECP70`, gives an explicit reconstruction framework for monotone paths from their signatures.

The moment step in Section 2 is even more elementary: it is the compact Hausdorff moment uniqueness consequence of polynomial density in `C([0,\log2])`. Directed searches across path-signature uniqueness, monotone/time-augmented signature inversion, and iterated-integral reconstruction did not produce a reason to regard the decoder mechanism itself as new.

No novelty is therefore claimed for signature uniqueness, moment inversion, or time/monotone-coordinate reconstruction. The line-specific exact consequence is the specialization to the Prime-Circle radial forms: **the single intrinsic shell `2` already supplies a monotone coordinate for which the one-sided words `2^k n` recover every cyclotomic shell profile, while the Mangoldt selector is only their zeroth moment.** That specialization sharpens the boundary left open by PC-347 but remains a classicalization result, not a new RH mechanism.

## 7. Boundary and consequence for Prime Circle

PC-347 left infinite-depth/nonnilpotent radial ordering open because fixed depth does not control a genuinely resummed holonomy. PC-399 does not prove that every such holonomy is trivial. It proves a different and necessary distinction:

**infinite-depth information gain is no longer evidence of a mechanism.** Even a tiny canonical subladder already becomes injective for the original shell profile, and that injectivity is reproduced by arbitrary non-arithmetic profiles.

A surviving nonperturbative radial construction must therefore do more than preserve or reconstruct shell data. It must derive from Prime-Circle geometry a **specific compression, representation, multiplication law, sign/coercivity form, spectral invariant, or cross-level evolution** whose relevant output is not reproduced by the generic moment decoder and whose zeta-facing consequence survives matched controls.

In particular, replacing the finite Chen truncation of PC-347 by the universal full signature does not by itself escape classicalization. The full signature is an information-rich coordinate system. The still-open question is whether the roots/refinement geometry forces a mathematically distinguished operation *on that information* with a nonclassical RH-relevant consequence.

## Audit / falsification tests

This finding fails if any of the following occurs:

1. `X_2(z)=log(1+z)` is not one-to-one on `[0,1]`;
2. the simplex reduction (8) does not hold with the word ordering used in PC-347;
3. two distinct finite signed measures on `[0,log2]` have all polynomial moments equal;
4. equality of the pushed-forward measures under the homeomorphism `X_2` does not imply equality of `dX_n`;
5. a non-prime-power shell has `dX_n=0` despite `\Phi_n` being a nonconstant cyclotomic polynomial.

All five checks are exact. The result makes no claim that a finite prefix of the ladder determines `n`, no quantitative stability claim for noisy/truncated moments, and no no-go claim for source-forced nonlinear or cross-level readouts that use the recovered information in a genuinely additional way.