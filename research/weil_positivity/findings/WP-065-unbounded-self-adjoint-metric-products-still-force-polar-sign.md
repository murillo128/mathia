# WP-065 — unbounded self-adjoint metric products still force the polar sign

**Status:** `EXACT-DERIVED + DECISIVE-BOUNDARY + CLASSICAL-MECHANISM + PRIOR-ART-REDIRECTION`. `WP-064` closes every bounded self-adjoint left-metric repair of the full-root `q=2` Hardy channel and leaves an explicitly domain-sensitive escape: perhaps an **unbounded** self-adjoint metric could make the signed channel positive without importing its spectral sign. Under the natural operator-level interpretation of that proposal, the escape also collapses. If `A` is bounded, self-adjoint and injective, `J` is an arbitrary self-adjoint operator, and the maximal product `-JA` is itself a positive self-adjoint operator, then `J` is necessarily the polar sign of `A` multiplied by a positive self-adjoint operator strongly commuting with `A`. The boundedness hypothesis on the metric in `WP-064` was therefore not responsible for the polar-sign obstruction.

This is a classical spectral/domain mechanism rather than a theorem-level novelty claim. Unbounded metric operators and the domain subtleties of quasi-Hermitian products are standard; see J.-P. Antoine and C. Trapani, *Partial inner product spaces, metric operators and generalized hermiticity*, J. Phys. A 46 (2013), 025204, DOI `10.1088/1751-8113/46/2/025204`, and K. Gustafson and M. H. Mortad, *Conditions implying commutativity of unbounded self-adjoint operators and related topics*, J. Operator Theory 76 (2016), 159–169, DOI `10.7900/jot.2015oct16.2076`. The durable Mathia-specific content is the exact closure of the unbounded left-metric route left open by `WP-064`, together with a precise statement of what genuinely more singular form-level constructions remain outside the no-go.

## 1. Exact operator-level question left open by `WP-064`

Let `A` be a bounded self-adjoint injective operator on a Hilbert space `H`:

\[
A=A^*,
\qquad
\ker A=0.
\tag{1}
\]

Let `J=J^*` be a possibly unbounded self-adjoint operator with dense domain. The natural maximal product is

\[
JA,
\qquad
\operatorname{Dom}(JA)
=
\{x\in\mathcal H:Ax\in\operatorname{Dom}J\}.
\tag{2}
\]

Suppose the proposed metric repair is an honest positive operator in the strongest ordinary sense:

\[
\boxed{
P:=-JA\ \text{is self-adjoint and}\ P\succeq0.
}
\tag{3}
\]

The question is whether unboundedness of `J` can evade the bounded classification of `WP-064`.

It cannot. Write

\[
A=\operatorname{sgn}(A)|A|.
\tag{4}
\]

Because `A` is injective, `sgn(A)` is a bounded self-adjoint unitary. Then (3) holds **if and only if** there exists a positive self-adjoint operator `K` which strongly commutes with `A` such that

\[
\boxed{
J=-K\operatorname{sgn}(A),
\qquad
-JA=K|A|\succeq0.
}
\tag{5}
\]

Thus the entire unbounded self-adjoint left-metric class has the same sign factor as the bounded class. Unboundedness changes only the positive spectral weight `K`.

## 2. Self-adjointness of the product already forces domain invariance and commutation

Assume (3). Since `JA` is self-adjoint,

\[
(JA)^*=JA.
\tag{6}
\]

For bounded `A=A^*` and self-adjoint `J`, the standard adjoint inclusion gives

\[
AJ\subseteq(JA)^*.
\tag{7}
\]

Combining (6) and (7),

\[
\boxed{AJ\subseteq JA.}
\tag{8}
\]

This inclusion contains the domain statement that matters. For every `x in Dom J`,

\[
Ax\in\operatorname{Dom}J,
\qquad
JAx=AJx.
\tag{9}
\]

So the bounded operator `A` preserves the domain of `J` and commutes with `J` there.

The apparently weak relation (9) upgrades to **strong commutation**. Fix `z notin R` and put

\[
x=(J-z)^{-1}y.
\]

Then `x in Dom J`, and (9) yields

\[
(J-z)Ax
=A(J-z)x
=Ay.
\]

Uniqueness of the resolvent solution gives

\[
\boxed{
A(J-z)^{-1}=(J-z)^{-1}A.
}
\tag{10}
\]

Hence `A` commutes with the resolvent and therefore with every spectral projection of `J`. Since `A` is bounded self-adjoint, its own bounded Borel functional calculus also commutes with the spectral resolution of `J`. In particular,

\[
|A|
\quad\text{and}\quad
\operatorname{sgn}(A)
\]

strongly commute with `J`.

This is the decisive domain step. Positivity has not yet been used; mere self-adjointness of the proposed product already prevents an arbitrary domain-dependent twist between `J` and `A`.

## 3. The polar factorization survives unchanged for unbounded `J`

Define

\[
\boxed{
K:=-J\operatorname{sgn}(A).
}
\tag{11}
\]

Because `sgn(A)` is a bounded self-adjoint unitary strongly commuting with `J`, the operator `K` is self-adjoint on `Dom J`. It strongly commutes with `A`, `|A|`, and `sgn(A)`. Using (4),

\[
-JA
=J(-A)
=K|A|.
\tag{12}
\]

The domains also agree exactly. Strong commutation implies that `sgn(A)` preserves `Dom K=Dom J`, so

\[
Ax\in\operatorname{Dom}J
\iff
|A|x\in\operatorname{Dom}K.
\tag{13}
\]

Thus (12) is not a formal identity on a convenient core; it is an equality of the maximal operator products occurring in (3).

It remains only to show that positivity of `K|A|` forces positivity of `K`. The possible accumulation of the spectrum of `|A|` at zero is exactly where an unbounded metric might have seemed able to hide a sign change. Injectivity rules that out.

## 4. Spectral cutoffs away from zero force `K` itself to be positive

Set

\[
B:=|A|\succeq0.
\]

For `epsilon>0`, let

\[
E_\varepsilon
=
\mathbf 1_{[\varepsilon,\|A\|]}(B).
\tag{14}
\]

Since `ker B=0`,

\[
E_\varepsilon\uparrow I
\qquad(\varepsilon\downarrow0)
\tag{15}
\]

strongly. Strong commutation of `B` and `K` implies that every `E_epsilon` reduces `K` and that

\[
KE_\varepsilon x=E_\varepsilon Kx
\qquad(x\in\operatorname{Dom}K).
\tag{16}
\]

On `E_epsilon H`, the operator `B^{-1/2}` is bounded. Take

\[
x\in\operatorname{Dom}K\cap E_\varepsilon\mathcal H,
\qquad
y=B^{-1/2}x.
\]

The strong commutation guarantees `y in Dom(KB)` and gives

\[
\begin{aligned}
0
&\le \langle KBy,y\rangle\\
&=\langle Kx,x\rangle.
\end{aligned}
\tag{17}
\]

Therefore `K` is nonnegative on every spectral region where `B` is bounded away from zero. For arbitrary `x in Dom K`, equations (15)–(16) give

\[
E_\varepsilon x\to x,
\qquad
K E_\varepsilon x\to Kx,
\tag{18}
\]

so the cutoff vectors converge in the graph norm of `K`. Taking the limit in (17) yields

\[
\boxed{
\langle Kx,x\rangle\ge0
\quad(x\in\operatorname{Dom}K),
}
\tag{19}
\]

hence

\[
\boxed{K\succeq0.}
\tag{20}
\]

Equivalently, the joint spectral theorem writes `K` and `B` as multiplication by real functions `k` and `b>=0`. Injectivity of `A` means `b>0` almost everywhere, while positivity of `KB` says `kb>=0`; therefore `k>=0` almost everywhere. The cutoff proof above is the domain-explicit version of the same fact.

Combining (11) and (20) proves the forward direction of (5).

## 5. Converse: every positive strongly commuting weight gives a positive self-adjoint product

Now let `K` be any positive self-adjoint operator strongly commuting with `A`, and define

\[
J=-K\operatorname{sgn}(A),
\qquad
\operatorname{Dom}J=\operatorname{Dom}K.
\tag{21}
\]

Because the bounded unitary `sgn(A)` strongly commutes with `K`, `J` is self-adjoint. Moreover,

\[
-JA=K|A|.
\tag{22}
\]

Strong commutation supplies a joint spectral representation in which the right-hand side is multiplication by the nonnegative function `k|a|`. Hence the maximal product is positive and self-adjoint.

Therefore the exact classification is

\[
\boxed{
-JA\succeq0\text{ self-adjoint}
\iff
J=-K\operatorname{sgn}(A)
\text{ for some }K\succeq0\text{ self-adjoint strongly commuting with }A.
}
\tag{23}
\]

The bounded theorem of `WP-064` is simply the special case in which `K`, hence `J`, is bounded.

## 6. Unboundedness really can produce repairs — but only the maximally circular ones

A useful matched control prevents a misleading interpretation of (23). The theorem does **not** say that unbounded repairs cannot exist. They can be extremely strong.

Take

\[
\mathcal H=L^2(-1,1),
\qquad
(Af)(x)=x f(x).
\tag{24}
\]

Then `A` is bounded, self-adjoint and injective, while

\[
(Jf)(x)=-\frac1x f(x)
\tag{25}
\]

is a densely defined unbounded self-adjoint operator. On the maximal product domain,

\[
\boxed{-JA=I.}
\tag{26}
\]

So domain sensitivity can apparently turn a sign-changing bounded operator into the identity. But (23) identifies exactly what happened:

\[
K=|A|^{-1},
\qquad
J=-|A|^{-1}\operatorname{sgn}(A).
\tag{27}
\]

The metric first determines the sign of `A` and then inverts its magnitude. It is the polar repair in its most singular possible form, not an independent positivity theorem.

This control is completely non-arithmetic. It shows both why the unbounded route had to be checked and why mere existence of a domain-sensitive positive product cannot count as a Weil mechanism.

## 7. Application to the selected Mathia `q=2` Hardy channel

For the full-root channel of `WP-061`–`WP-064`,

\[
F:=\mathcal F_2
=
\begin{pmatrix}
0&-H\\
-H&0
\end{pmatrix},
\tag{28}
\]

with `H` the positive injective Hilbert matrix. `WP-063` gives

\[
|F|=H\oplus H,
\qquad
\operatorname{sgn}(F)=-S,
\tag{29}
\]

where

\[
S=
\begin{pmatrix}
0&I\\
I&0
\end{pmatrix}
\tag{30}
\]

is the canonical adjacent-parity swap.

Applying (23), every possibly unbounded self-adjoint left multiplier for which the maximal product is a positive self-adjoint operator has the form

\[
\boxed{
J=KS,
\qquad
K\succeq0,
\qquad
K\text{ strongly commutes with }F,
}
\tag{31}
\]

and the repaired operator is

\[
\boxed{
-JF=K|F|.
}
\tag{32}
\]

Thus the route left open at the end of `WP-064` does not acquire a new sign mechanism merely by allowing `K` to become unbounded. The same canonical sign operator `S=-sgn(F)` is still compulsory.

There is an even sharper consequence if “metric operator” is used in the standard Hilbert-space sense `J>=0`. Let `E_+` be the positive spectral projection of `F`. Since `K` strongly commutes with `F`, on `E_+ H` equation (23) gives

\[
J=-K.
\tag{33}
\]

If both `J>=0` and `K>=0`, then `K` and `J` must vanish on the entire positive spectral subspace. `WP-062` proves that this subspace has infinite dimension. Therefore

\[
\boxed{
J\succeq0,
\quad
-JF\succeq0\text{ self-adjoint}
\Longrightarrow
J E_+=0.
}
\tag{34}
\]

In particular, **no strictly positive self-adjoint metric operator, bounded or unbounded, can repair the full-root channel by left multiplication**. An indefinite unbounded metric can do so, but only by carrying the polar sign explicitly as in (31).

## 8. What remains genuinely outside the no-go

The hypothesis in (3) is deliberately strong and audit-friendly. It treats the proposed positivity as an actual self-adjoint operator product on its maximal natural domain. The conclusion must not be stretched beyond that class.

The following routes remain logically open:

1. a positive **closed quadratic form** obtained from a smaller core when the maximal product `JA` is not self-adjoint, followed by a Friedrichs-type closure or another independently forced extension;
2. a renormalized/singular form in which the positive object is not the operator product `JA` at all;
3. a non-self-adjoint intertwiner whose positivity emerges only after a larger block construction;
4. a quotient or compression selected by additional Mathia geometry rather than left multiplication;
5. most importantly, a nonseparable finite-prime/archimedean/polar construction in which the three sectors are coupled before the final sign theorem.

These are not semantic loopholes. Unbounded operator products are genuinely domain-sensitive, and form positivity can survive in situations where a naive product is not self-adjoint. But after this finding, invoking only “an unbounded metric” is no longer a distinct escape. A surviving proposal must specify a different positive object and show exactly why it lies outside (3).

## 9. Prior-art and novelty audit

The abstract ingredients in (6)–(23) are classical functional analysis: adjoints of bounded–unbounded products, resolvent commutation, strong commutation of self-adjoint operators, joint spectral calculus, and polar decomposition. The literature on unbounded metric operators explicitly emphasizes that domains and changes of Hilbert scale are the central additional issue; Antoine–Trapani (2013, DOI `10.1088/1751-8113/46/2/025204`) is a direct prior-art anchor. Gustafson–Mortad (2016, DOI `10.7900/jot.2015oct16.2076`) likewise studies when products of bounded and unbounded self-adjoint operators become self-adjoint and when that forces commutativity.

Accordingly, no novelty is claimed for theorem (23) as abstract operator theory. The matched multiplication example (24)–(27) further shows that the mechanism is universal and has no arithmetic content.

The Mathia-specific durable conclusion is narrower: `WP-064` explicitly left the unbounded/domain-sensitive metric as a possible escape from the `q=2` Hardy polar-sign classification. Under the natural maximal-product formulation, that escape is now closed exactly. The only residual domain-sensitive direction is **form-level or extension-level geometry that is not equivalent to making `-JF` itself a positive self-adjoint product**.

This remains well separated from classical Weil positivity, Hilbert–Pólya, Connes/trace formulas, and cohomological intersection routes. Nothing here realizes the completed Weil functional, zero measure, Gamma response, or polar term. It is a no-go about one proposed source of an independent sign theorem.

## 10. Falsification surface and research consequence

The claim has a short exact audit surface.

1. Verify the adjoint inclusion `AJ subset (JA)*` for bounded `A` and self-adjoint `J`.
2. Under self-adjointness of `JA`, deduce `AJ subset JA`, including the domain invariance in (9).
3. Use the resolvent calculation (10) to prove strong commutation of `A` and `J`.
4. Verify that `K=-J sgn(A)` is self-adjoint and strongly commuting with `A`.
5. Check equality of the maximal product domains in (13) and the identity `-JA=K|A|`.
6. Use the spectral cutoffs (14)–(19) to prove `K>=0` without assuming `|A|` is bounded below.
7. Verify the converse by joint spectral calculus.
8. Run the multiplication control (24)–(27), where an explicitly unbounded repair gives the identity and nevertheless factors exactly through the polar sign.
9. Apply the theorem to `F`, using `sgn(F)=-S` from `WP-063`, and verify (31)–(34).

Failure at any of steps 1–7 invalidates the classification. Their success narrows the frontier to a substantially more specific problem:

\[
\boxed{
\text{a successful domain-sensitive escape must be genuinely form/extension based,}
\quad
\text{not merely an unbounded self-adjoint multiplier with }-JF\ge0.
}
\]

For the main `weil_positivity` mandate, even such a form-level escape would still have to do much more: one canonical construction must simultaneously retain the sparse finite Mangoldt term, the full-root `q=2` archimedean response, and the polar/global counterterms, with nonnegativity supplied independently by the geometry. `WP-065` removes unbounded left-metric multiplication from that search space.