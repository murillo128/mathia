# MC-181 — The logarithmic rough Möbius split is subpower-reversible on local variance

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-180` proved an exponent-preserving forward transfer from a logarithmically rough Möbius factor to the full Möbius short-interval variance. The same split also has a converse transform whose cost is only subpower at the logarithmic cutoff.

Keep the notation of `MC-180`. Thus

\[
y=c\log X,
\qquad
0<c<\min(\theta,1-\theta),
\qquad
H=X^\theta,
\]

and

\[
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y}.
\]

Define the all-powers smooth indicator

\[
s_y(d)=\mathbf 1_{P^+(d)\le y},
\qquad s_y(1)=1.
\]

Then there is the exact inverse convolution identity

\[
\boxed{g_y=\mu*s_y.}
\tag{1}
\]

Indeed, at every prime `p<=y` the local factors `(1-z)(1+z+z^2+...)` cancel to `1`, while for `p>y` the smooth factor is `1` and the Möbius factor remains `1-z`.

For

\[
S_\mu(u,L)=\sum_{u<m\le u+L}\mu(m),
\qquad
R_y(x,H)=\sum_{x<n\le x+H}g_y(n),
\]

(1) gives

\[
\boxed{
R_y(x,H)
=
\sum_{\substack{d\le x+H\\P^+(d)\le y}}
S_\mu\!\left(\frac xd,\frac Hd\right).
}
\tag{2}
\]

Let

\[
V_\mu(U,L)=\int_U^{2U}|S_\mu(u,L)|^2\,du,
\qquad
V_y(X,H)=\int_X^{2X}|R_y(x,H)|^2\,dx,
\]

and write `Psi(Z,y)` for the number of `y`-smooth integers at most `Z`. Cauchy--Schwarz in (2), followed by `u=x/d`, yields the unconditional reverse-transfer inequality

\[
\boxed{
V_y(X,H)
\le
\Psi(3X,y)
\sum_{\substack{d\le3X\\P^+(d)\le y}}
 d\,V_\mu\!\left(\frac Xd,\frac Hd\right).
}
\tag{3}
\]

At the logarithmic cutoff the apparent all-powers inverse kernel is still subpower:

\[
\boxed{\Psi(3X,c\log X)=X^{o(1)}.}
\tag{4}
\]

Consequently fix `0<eta<=1`. If, uniformly for every `y`-smooth `d<=H`,

\[
V_\mu\!\left(\frac Xd,\frac Hd\right)
\le
X^{o(1)}\frac Xd\left(\frac Hd\right)^{2-\eta},
\tag{5}
\]

then

\[
\boxed{
V_y(X,H)
\le X^{1+o(1)}H^{2-\eta}.
}
\tag{6}
\]

Thus the logarithmic prime split of `MC-180` is not an information-losing relaxation at the fixed-power variance level. On scale families stable under the required small-prime dilations, the rough and full Möbius coefficient systems transfer the same exponent with at most `X^{o(1)}` loss in either direction: `MC-180` supplies rough-to-full, while (1)--(6) supply full-to-rough.

This does **not** say that the two estimates are equally difficult to prove. The rough factor may expose a proof structure unavailable in the unsifted coefficients. It says that any advantage must come from such proof structure, not from having weakened the fixed-power variance target by discarding small-prime information.

## 1. The inverse kernel is exact

The Dirichlet-series/Euler-factor calculation behind (1) is purely algebraic. For a prime power `p^k`, the convolution of `mu` with `s_y` has local coefficients

\[
(1,-1,0,\ldots)*(1,1,1,\ldots)=(1,0,0,\ldots)
\]

when `p<=y`, and

\[
(1,-1,0,\ldots)*(1,0,0,\ldots)=(1,-1,0,\ldots)
\]

when `p>y`. Multiplicativity therefore proves (1) coefficientwise, with no analytic continuation or zero-free information.

Summing (1) over `(x,x+H]` and grouping by the smooth divisor `d` gives (2). For `x in [X,2X]` and `H<=X`, only `d<=3X` can occur. There are at most `Psi(3X,y)` summands, so

\[
|R_y(x,H)|^2
\le
\Psi(3X,y)
\sum_{\substack{d\le3X\\P^+(d)\le y}}
\left|S_\mu\!\left(\frac xd,\frac Hd\right)\right|^2.
\]

Integration and the substitution `u=x/d` prove (3).

## 2. Logarithmically smooth integers are only a subpower family

A crude Rankin bound is already enough for (4). Put

\[
\sigma=\frac1{\log y}.
\]

Then

\[
\Psi(3X,y)
\le
(3X)^\sigma
\prod_{p\le y}(1-p^{-\sigma})^{-1}.
\tag{7}
\]

For `p<=y`, the elementary inequality `1-e^{-t} >= t/2` on `0<t<=1` gives

\[
(1-p^{-\sigma})^{-1}
\ll \frac{\log y}{\log p}
\ll \log y.
\]

Using only the standard bound `pi(y)=O(y/log y)`, the logarithm of the Euler product in (7) is therefore

\[
O\!\left(\frac{y\log\log y}{\log y}\right)=o(\log X)
\]

when `y=c log X`; also

\[
(3X)^\sigma
=
\exp\!\left(O\!\left(\frac{\log X}{\log\log X}\right)\right)
=X^{o(1)}.
\]

This proves (4). The distinction from the square-free small-prime kernel of `MC-180` is important: the inverse kernel allows arbitrary powers of primes at most `y`, but at a logarithmic cutoff even the full smooth family remains subpower up to height `X`.

## 3. Fixed-power variance survives the inverse transform

Split the sum in (3) at `d=H`.

For `d<=H`, insert (5). The `d`-th term is

\[
d\,V_\mu(X/d,H/d)
\le
X^{1+o(1)}H^{2-\eta}d^{\eta-2}.
\]

If `0<eta<1`, then

\[
\sum_{P^+(d)\le y}d^{\eta-2}
\le \zeta(2-\eta)<\infty.
\]

For `eta=1`, the corresponding smooth harmonic sum is

\[
\sum_{P^+(d)\le y}\frac1d
=
\prod_{p\le y}(1-p^{-1})^{-1}
=X^{o(1)},
\]

where the final subpower estimate follows already from the same crude product bound used in Section 2. Hence the total `d<=H` contribution to (3), including the outer factor (4), is `X^{1+o(1)}H^{2-eta}`.

For `d>H`, the scaled interval has length `H/d<1`. Such an interval contains at most one integer. If `U=X/d` and `L=H/d`, the set of `u in [U,2U]` for which `(u,u+L]` contains an integer has measure at most `O((U+1)L)`. Therefore

\[
d\,V_\mu(X/d,H/d)
\ll
H\left(\frac Xd+1\right).
\tag{8}
\]

Summing (8) over `y`-smooth `d<=3X`, then using (4) and the subpower bound for the smooth reciprocal sum, gives after the outer Cauchy factor

\[
X^{1+o(1)}H.
\]

Because `eta<=1`, this is at most `X^{1+o(1)}H^{2-eta}`. Combining the two ranges proves (6).

## 4. What this changes about the live rough-parity target

`MC-180` correctly identifies a useful reorganization: square-free support eliminates the pure logarithmically smooth Möbius sector on `[X,2X]`, and all large primes can be kept inside one signed rough factor. The present inverse shows that this reorganization is algebraically more faithful than the one-way calculation alone reveals.

At polynomial local scales, the all-powers smooth inverse has only subpower complexity. Therefore the rough block cannot gain a fixed exponent merely because small primes were removed. If a proof of the rough variance target succeeds, the gain must use a feature that becomes analytically accessible after sifting -- for example a parity-sensitive bilinear decomposition, a Type-II estimate, or another signed coupling -- while surviving the exponent-preserving reconstruction back to `mu`.

This sharpens the research question from "is the rough block easier?" to a falsifiable form: **what theorem becomes provable for `g_y` after removing the first `c log X` primes that is not already available for `mu`, even though the two coefficient systems are connected by subpower-cost dilation transforms?**

## 5. The obvious general short-interval theorem does not directly cover the moving rough factor

A prior-art check against Matomäki--Radziwiłł, *Multiplicative functions in short intervals II*, arXiv:2007.04290, gives an additional boundary. Their Definition 1.8 and Theorem 1.9 treat `(alpha,Delta)`-non-vanishing multiplicative functions, requiring for a fixed `alpha>0`

\[
\sum_{w<p\le z}\frac{|f(p)|}{p}
\ge
\alpha\sum_{w<p\le z}\frac1p-O(1/\log w)
\]

through all prime ranges up to the theorem scale. For the moving rough coefficient `g_y`,

\[
|g_y(p)|=0\quad(p\le y),
\qquad
|g_y(p)|=1\quad(p>y).
\]

Taking `w=2` and `z=y` makes the left side zero while the prime-harmonic mass on the right grows like `alpha log log y` up to an additive constant. Thus the family `g_{c log X}` does not satisfy their fixed-positive-`alpha` non-vanishing hypothesis uniformly, and Theorem 1.9 is not a black-box proof of the live rough-block estimate.

The same paper also separates two rates that matter here: it obtains power saving in the **size of the exceptional set**, while its introduction explicitly notes that the generic `o(1)` discrepancy between normalized short and long averages cannot in general be replaced by `h^{-c}` for fixed `c>0`. This is consistent with `MC-001`: power control of exceptional frequency alone is not the fixed-power amplitude/variance gain needed by `MC-180`.

This does not rule out adapting Matomäki--Radziwiłł machinery to the special moving initial-prime cutoff. It says such an adaptation must use more than the published theorem as a black box and must confront exactly the source-specific signed rough-parity structure isolated by `MC-180`.

## 6. Prior art and novelty assessment

The rough sum itself is classical. As already audited in `MC-180`, Alladi's 1982 work studies

\[
\sum_{n\le x,\,P^-(n)>y}\mu(n),
\]

and later restricted-prime-factor literature treats the same family. The prime split, the Euler-factor inverse (1), Rankin's smooth-number bound, and Cauchy--Schwarz are standard mechanisms; **no novelty is claimed for any of them individually**.

The durable contribution here is the combined rate audit: at `y=c log X`, the inverse all-powers smooth kernel is `X^{o(1)}` up to height `X`, and this is enough to preserve every fixed variance exponent `0<eta<=1` on the natural dilation family. This closes an information-direction left open by `MC-180` and shows that the logarithmic rough split is an exponent-preserving change of proof coordinates rather than a fixed-power relaxation.

The Matomäki--Radziwiłł check additionally prevents a false shortcut: their powerful sparse/vanishing multiplicative-function theorem requires a fixed positive non-vanishing density across prime ranges, whereas `g_y` deliberately deletes the entire initial prime segment.

## 7. Boundaries and falsification tests

- The converse transfer (6) assumes the full-Möbius variance estimate (5) uniformly over the `y`-smooth dilations that appear in the exact inverse. A bound at only the single pair `(X,H)` is not claimed to imply the rough estimate at that pair.
- Conversely, `MC-180` requires rough-block control over its square-free divisor-scaled family. The two directions give exponent-level equivalence only for scale families closed under the respective logarithmic small-prime dilations.
- Subpower invertibility is specific to the logarithmic cutoff. If `y` grows like a fixed power of `X`, `Psi(X,y)` is no longer subpower, and the argument does not preserve a fixed exponent for free.
- Equation (1) uses all powers of small primes. Replacing `s_y` by the square-free divisor indicator is false and would not invert the split.
- The result does not prove the live rough variance estimate, a Mertens power bound, or RH. It constrains what an eventual proof must gain from the rough representation.
- The Matomäki--Radziwiłł non-vanishing failure is a statement about direct applicability of their published fixed-`alpha` theorem. It is not a no-go theorem for adaptations of their proof architecture.
- Any proposed advantage of the rough block should now be tested against the inverse transform: if the claimed gain depends only on sparsity or on having fewer coefficients, it must explain why the `X^{o(1)}` smooth reconstruction does not erase that advantage.