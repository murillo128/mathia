# MC-258 — Squarefree conductor descent is exactly compensated in the blind-projector normalization

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell-square blind-projector setting of `MC-246` and the wild-Sylow collapse of `MC-257`. Put

\[
R=\prod_{r\in S}r,
\qquad
q=\prod_{r\in S}r^2=R^2,
\]

and write

\[
G_q=(\mathbb Z/q\mathbb Z)^\times,
\qquad
G_R=(\mathbb Z/R\mathbb Z)^\times.
\]

Let

\[
H_q=\langle p\bmod q:p\le y\text{ prime}\rangle,
\qquad
H_R=\langle p\bmod R:p\le y\text{ prime}\rangle,
\]

and let

\[
\pi:G_q\to G_R
\]

be reduction modulo `R`.

`MC-257` proves that the whole prime-square kernel

\[
U:=\ker\pi
\]

lies in `H_q`. Since `\pi(H_q)=H_R`, this implies the stronger exact identity

\[
\boxed{H_q=\pi^{-1}(H_R).}
\tag{1}
\]

Moreover

\[
|U|=R,
\qquad
|H_q|=R|H_R|,
\qquad
\varphi(q)=R\varphi(R).
\tag{2}
\]

Thus the complete blind character family modulo `q` is the inflation of the annihilator

\[
A_R:=H_R^\perp\le\widehat{G_R},
\]

and every primitive blind conductor divides the squarefree shell modulus `R`.

The important new point is what happens to the **exact source projector** of `MC-246`. Let

\[
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y},
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P.
\]

`MC-246` gives

\[
B_S^{(A)}(X)
=
\frac1{|H_q|}
\sum_{\substack{n\le T\\-n\bmod q\in H_q}}g_y(n).
\tag{3}
\]

Using `(1)` and `(2)`, membership descends exactly,

\[
-n\bmod q\in H_q
\iff
-n\bmod R\in H_R,
\tag{4}
\]

and therefore

\[
\boxed{
B_S^{(A)}(X)
=
\frac1{R|H_R|}
\sum_{\substack{n\le T\\-n\bmod R\in H_R}}g_y(n).
}
\tag{5}
\]

If

\[
\mathcal P_R(g;T,-1)
:=
\frac1{|H_R|}
\sum_{\substack{n\le T\\-n\bmod R\in H_R}}g(n)
\tag{6}
\]

is the natural full-annihilator projector at the **squarefree** modulus `R`, then

\[
\boxed{
B_S^{(A)}(X)=\frac1R\,\mathcal P_R(g_y;T,-1).
}
\tag{7}
\]

Hence the conductor descent `q=R^2 -> R` does **not** simply replace `q` by `R` in the support budget. The missing factor is retained exactly as an exterior normalization `1/R` inherited from the original square-modulus character expansion.

In particular, direct support counting from `(5)` gives

\[
\boxed{
|B_S^{(A)}(X)|
\le
\frac{T}{R^2}\frac{\varphi(P)}P
+O\!\left(\frac{2^{\pi(y)}}R\right).
}
\tag{8}
\]

The main term is exactly the `MC-246` main term because `R^2=q`. Thus at

\[
y=c\log X,
\qquad
R=X^{\alpha+o(1)},
\]

with fixed `alpha>0`,

\[
\boxed{
|B_S^{(A)}(X)|
\ll
\frac{X^{1-2\alpha+o(1)}}{\log\log X}
+X^{-\alpha+o(1)}.
}
\tag{9}
\]

The conductor descent improves the elementary inclusion-exclusion error by a factor `R`, but it leaves the support exponent unchanged. In particular, **support alone still reaches the square-root scale only at `alpha>=1/4`**. The post-`MC-257` gain is therefore analytic rather than combinatorial: every blind twist now has squarefree conductor dividing `R`, so a genuine improvement must exploit cancellation available at conductor `R`, not merely recount the same coset at the smaller modulus.

No new estimate for the squarefree-conductor twisted Möbius sums, no improvement of the `alpha=1/4` support boundary, no proof that `H_R=G_R`, and no consequence for `M(X)` or the zeta zero set is obtained.

## 1. The small-prime subgroup is exactly the full preimage after wild collapse

Reduction modulo `R` maps every small-prime generator of `H_q` to the corresponding generator of `H_R`, hence

\[
\pi(H_q)=H_R.
\tag{10}
\]

`MC-257` proves

\[
U=\ker\pi\subseteq H_q.
\tag{11}
\]

The inclusion

\[
H_q\subseteq\pi^{-1}(H_R)
\]

is immediate from `(10)`. Conversely, if `x\in\pi^{-1}(H_R)`, choose `h\in H_q` with

\[
\pi(h)=\pi(x).
\]

Then

\[
xh^{-1}\in U\subseteq H_q,
\]

so `x\in H_q`. This proves `(1)`.

For each shell prime `r`, the kernel of

\[
(\mathbb Z/r^2\mathbb Z)^\times
\to
(\mathbb Z/r\mathbb Z)^\times
\]

has order `r`. Chinese remaindering therefore gives

\[
|U|=\prod_{r\in S}r=R,
\]

which proves the subgroup-size relation in `(2)`. The Euler-phi identity follows independently from

\[
\varphi(r^2)=r\varphi(r)
\]

for each shell prime.

Equation `(4)` is now just the preimage identity `(1)`. If `n` is divisible by a shell prime, then `-n` is a nonunit modulo both `q` and `R` and belongs to neither unit subgroup, so no hidden exceptional case is introduced by the descent.

## 2. The character-side formula retains the same factor exactly

Let

\[
A_q:=H_q^\perp\le\widehat{G_q}.
\]

Because `U\subseteq H_q`, every `\chi\in A_q` is trivial on `U` and therefore factors uniquely through `G_R`. Inflation along `\pi` gives an isomorphism

\[
\boxed{A_R\cong A_q.}
\tag{12}
\]

For a Dirichlet character `\psi mod R`, let the same symbol denote its inflation modulo `q`. The two characters agree on integers coprime to the shell primes, and both vanish on integers sharing a shell prime because `q` and `R` have the same prime support. Hence the twisted sums are literally the same arithmetic sums:

\[
S_{g_y}(T,\psi)
:=
\sum_{n\le T}g_y(n)\psi(n).
\tag{13}
\]

Applying the ordinary character projector at modulus `R` and using `(2)` gives the equivalent form of `(7)`:

\[
\boxed{
B_S^{(A)}(X)
=
\frac1{R\varphi(R)}
\sum_{\psi\in A_R}
\overline{\psi(-1)}S_{g_y}(T,\psi)
=
\frac1R\mathcal P_R(g_y;T,-1).
}
\tag{14}
\]

This identity is the correct interface for any post-`MC-257` analytic argument. Replacing the square modulus by the primitive/squarefree conductor is legitimate, but dropping the factor `1/R` is not.

Conversely, the factor `1/R` is potentially useful only together with a genuinely stronger estimate for the squarefree-conductor projector or its twisted sums. Equation `(14)` by itself is an exact re-expression of the same source and therefore supplies no cancellation.

## 3. Inclusion-exclusion at modulus `R` reproduces the old main exponent

Let

\[
A_{H_R}(U)
:=
\#\{m\le U:-m\bmod R\in H_R\}.
\]

A complete interval of length `R` contains exactly `|H_R|` residues in the coset `-H_R`, so

\[
A_{H_R}(U)
=
\frac{|H_R|}{R}U+O(|H_R|).
\tag{15}
\]

Every divisor `d|P` is a unit modulo `R` and belongs to `H_R`. Therefore

\[
-dm\in H_R
\iff
-m\in H_R.
\]

Inclusion-exclusion gives

\[
\begin{aligned}
C_{H_R}(T)
&:=
\#\{n\le T:-n\bmod R\in H_R,(n,P)=1\}\\
&=
\sum_{d\mid P}\mu(d)A_{H_R}(T/d)\\
&=
\frac{|H_R|T}{R}\frac{\varphi(P)}P
+O\!\left(|H_R|2^{\pi(y)}\right).
\end{aligned}
\tag{16}
\]

The support of `g_y` is contained in the set counted by `C_{H_R}(T)`. Dividing `(16)` by the exact normalization `R|H_R|` in `(5)` proves `(8)`.

At `y=c log X`, Mertens' product theorem gives

\[
\frac{\varphi(P)}P
\asymp
\frac1{\log y}
\asymp
\frac1{\log\log X},
\tag{17}
\]

while

\[
2^{\pi(y)}=X^{o(1)}.
\tag{18}
\]

If `R=X^{\alpha+o(1)}` with fixed `alpha>0`, equations `(8)`, `(17)`, and `(18)` give `(9)`.

The support threshold is therefore unchanged:

\[
1-2\alpha\le\frac12
\iff
\alpha\ge\frac14.
\tag{19}
\]

This is not a contradiction with conductor descent. The set of admissible residues becomes denser when the modulus is reduced from `R^2` to `R`, by exactly the factor needed to compensate for the smaller period after the inherited `1/R` normalization is retained.

## 4. What MC-257 really buys analytically

`MC-257` removes all wild prime-square character directions. Equation `(14)` shows the exact remaining opportunity:

- every blind character is induced from a character of squarefree conductor dividing `R`;
- the arithmetic source is still the same rough Möbius function `g_y`;
- the aggregate projector carries the exterior `1/R` factor;
- support counting alone cannot exploit the smaller conductor beyond the improved error term.

Thus the next analytic question is not whether one may simply substitute `R` for `q` in `MC-246`; `(7)`--`(9)` show that this gives no new main exponent. The useful question is whether a theorem for **squarefree-conductor Möbius twists or their exact annihilator aggregate** supplies a cancellation factor that was unavailable at the shell-square conductor.

This also clarifies the relation to `MC-237`. That finding applies a smooth-modulus variance theorem directly at `q=R^2` and shows that its residual scale cannot beat the strict hard boundary. The present identity does not license rereading that theorem with `q=R`: its hypotheses, normalization, distinguished-character subtraction, and averaging measure must all be re-derived for the squarefree-conductor family. Any gain must come from a theorem that sees the reduced conductor at the level of cancellation, not from the algebraic descent alone.

## 5. Prior art and novelty boundary

The ingredients in `(1)`--`(14)` are classical finite-abelian and Dirichlet-character theory. A character modulo a composite modulus factors through a smaller modulus exactly when it is trivial on the corresponding reduction kernel; primitive conductor is the minimal modulus through which it factors. Character orthogonality on a subgroup and inflation from a quotient are standard. The Encyclopedia of Mathematics entry **Dirichlet character** records the primitive/imprimitive conductor distinction and the usual orthogonality relations; standard analytic-number-theory texts treat the same induction of imprimitive characters.

Mertens' product theorem supplies `(17)`. No novelty is claimed for character induction, conductor descent, subgroup orthogonality, Euler-phi identities, periodic residue counting, or inclusion-exclusion.

A targeted prior-art check did not identify a source treating this exact Mathia shell projector, but that absence is not used as a novelty claim. The durable contribution here is a **frontier accounting identity** obtained by composing two already-persisted shell facts: `MC-246`'s exact full-annihilator source projector and `MC-257`'s exact wild-kernel inclusion. It prevents the smaller conductor from being mistaken for a free support-level power gain and isolates the only remaining place where the descent can help: a genuinely conductor-sensitive cancellation estimate.

## 6. Boundaries and falsification audit

- The identity `H_q=pi^{-1}(H_R)` uses the full inclusion `ker pi subseteq H_q` from `MC-257`; without that input the normalization reduction is invalid.
- The modulus relation is exactly `q=R^2` because the shell primes are distinct and every shell factor occurs to exponent two.
- The character sums in `(14)` agree only because `q` and `R` have identical prime support; integers noncoprime to either modulus contribute zero to both character extensions.
- The support estimate counts a superset of the nonzero `g_y` terms and is therefore an upper bound, not an asymptotic for the signed Möbius source.
- Equation `(8)` must retain the exterior `1/R`. Omitting it would incorrectly change the main term from `T/R^2` to `T/R` and create a fictitious deterioration rather than the exact original projector.
- Conversely, replacing the original support density `1/R^2` by `1/R` while also forgetting that the coset normalization changes from `1/|H_q|` to `1/(R|H_R|)` would create a fictitious conductor gain. The two effects compensate exactly in the main term.
- No cancellation estimate for `S_{g_y}(T,psi)` is inferred from the conductor reduction. Any use of Burgess, large-sieve, zero-free, dispersion, or smooth-modulus results must recheck the actual range and source weights.

The decisive finite audit is direct. For any finite shell, compute `H_q`, `H_R`, and the reduction map; verify `H_q=pi^{-1}(H_R)`, `|H_q|=R|H_R|`, and then compare the two sides of `(5)` for arbitrary bounded test functions supported away from the shell primes. A discrepancy would identify an error in the subgroup or normalization descent rather than an analytic phenomenon.

## Updated frontier

The wild prime-square branch is now closed at both the group and support-budget levels. `MC-257` shows that wild Sylow directions do not survive; the present finding shows that the resulting conductor descent does not by itself move the `alpha=1/4` support boundary.

The remaining exits are correspondingly sharper: either prove additional **moving-shell tame cross-prime rigidity** strong enough to shrink the squarefree blind quotient, or obtain a **conductor-sensitive signed estimate** for the exact squarefree blind projector in `(14)` / rough Möbius coset in `(5)`. Any proposal that only observes that the primitive conductors are smaller, without producing such an estimate, is now classified as algebraic reparameterization rather than quantitative progress.