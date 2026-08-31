# WP-064 — bounded self-adjoint metric repairs force the polar sign

**Status:** `EXACT-DERIVED + DECISIVE-BOUNDARY + CLASSICAL-MECHANISM + PRIOR-ART-REDIRECTION`. `WP-063` classified the natural `D`-odd fundamental-symmetry repairs of the full-root `q=2` Hardy channel and left open a larger nonunitary metric. That bounded self-adjoint escape can now be classified completely. If a bounded self-adjoint multiplier `J` makes the signed Hardy channel positive, then `J` must contain the spectral sign of that same channel exactly; the only remaining freedom is a positive operator commuting with the channel. In particular, the `D`-odd hypothesis in the unitary uniqueness statement of `WP-063` was unnecessary: among **all** bounded self-adjoint involutions, positivity uniquely forces the polar sign.

The argument is general bounded operator theory, not a historically new theorem. Its Mathia-specific consequence is decisive: the full-root `q=2` channel cannot acquire an independent sign theorem by replacing the canonical parity swap with a bounded nonunitary self-adjoint metric. A positive Hilbert-space metric cannot repair the channel at all without annihilating an entire spectral half. Any boundedly invertible indefinite repair is merely the polar sign multiplied by a positive commuting weight.

## 1. Setup from `WP-061`–`WP-063`

For the canonically selected full-root field

\[
V_2(z)=\Log(1-z^2),
\]

`WP-061`–`WP-063` identify the Hardy operator

\[
F:=\mathcal F_2
=
\begin{pmatrix}
0&-H\\
-H&0
\end{pmatrix},
\qquad
H_{jk}=\frac1{j+k+1},
\tag{1}
\]

on `ell^2 ⊕ ell^2`. The Hilbert matrix `H` is bounded, positive, and injective. Hence `F` is bounded, self-adjoint, and injective.

Let

\[
S=
\begin{pmatrix}
0&I\\
I&0
\end{pmatrix}.
\tag{2}
\]

`WP-063` proves

\[
|F|=H\oplus H,
\qquad
\operatorname{sgn}(F)=-S,
\qquad
-SF=|F|.
\tag{3}
\]

It then shows that, if one additionally requires a self-adjoint unitary metric `J` to exchange the canonical even/odd sectors, positivity forces `J=S`.

The question here is whether dropping that parity-exchange constraint and allowing a general bounded nonunitary self-adjoint metric creates a genuinely different positive geometry.

## 2. General classification theorem

Let `A` be any bounded self-adjoint **injective** operator on a complex Hilbert space. Write

\[
A=\operatorname{sgn}(A)|A|.
\tag{4}
\]

Because `ker A=0`, the spectral sign is a self-adjoint unitary:

\[
\operatorname{sgn}(A)^2=I.
\tag{5}
\]

Let `J=J^*` be bounded. Then

\[
\boxed{
-JA\succeq0
}
\tag{6}
\]

holds **if and only if** there exists a bounded positive operator `K` commuting with `A` such that

\[
\boxed{
J=-K\,\operatorname{sgn}(A).
}
\tag{7}
\]

For such a `J`,

\[
\boxed{
-JA=K|A|\succeq0.
}
\tag{8}
\]

So every bounded self-adjoint left-metric repair contains the polar sign explicitly. There is no second bounded self-adjoint sign mechanism hidden behind a nonunitary metric.

### Proof

Assume first that (6) holds. Positivity implies self-adjointness, hence

\[
(-JA)^*=-AJ=-JA,
\]

so

\[
\boxed{JA=AJ.}
\tag{9}
\]

Since `A` is bounded and self-adjoint, the spectral theorem implies that every bounded operator commuting with `A` commutes with its spectral projections and therefore with both `|A|` and `sgn(A)`. Define

\[
K:=-J\operatorname{sgn}(A).
\tag{10}
\]

Then `K` is bounded and self-adjoint, commutes with `A`, and

\[
-JA
=K|A|.
\tag{11}
\]

Because `K` commutes with `|A|`,

\[
K|A|
=|A|^{1/2}K|A|^{1/2}.
\tag{12}
\]

Thus (6) implies

\[
\langle K y,y\rangle\ge0
\qquad
\text{for every }y\in\operatorname{Ran}|A|^{1/2}.
\tag{13}
\]

Injectivity of `A` implies `ker |A|^{1/2}=0`, hence

\[
\overline{\operatorname{Ran}|A|^{1/2}}=\mathcal H.
\tag{14}
\]

Since `K` is bounded, (13) extends by continuity to all `y`, so

\[
\boxed{K\succeq0.}
\tag{15}
\]

Equation (7) follows from (10).

Conversely, suppose `K\succeq0` is bounded and commutes with `A`, and define `J` by (7). Then `J=J^*` and

\[
-JA
=K\operatorname{sgn}(A)^2|A|
=K|A|.
\tag{16}
\]

The two positive operators `K` and `|A|` commute, so their product is positive. This proves the equivalence.

## 3. Applied to the Mathia `q=2` channel, every repair is `K S`

For `F=\mathcal F_2`, equation (3) gives

\[
\operatorname{sgn}(F)=-S.
\]

Therefore the classification becomes

\[
\boxed{
-JF\succeq0
\iff
J=KS,
\quad
K\succeq0,
\quad
KF=FK.
}
\tag{17}
\]

and every repaired operator is

\[
\boxed{
-JF=K|F|.
}
\tag{18}
\]

The canonical repair of `WP-063` is simply the case `K=I`.

This is stronger than the previous `D`-odd uniqueness statement. The metric is no longer assumed to anticommute with the Hardy half-turn `D`, to exchange parity sectors, or even to be unitary. Positivity itself first forces `J` to commute with `F`, and then forces its sign to be the polar sign of `F`.

## 4. Every fundamental-symmetry repair is uniquely the canonical parity swap

Suppose now that `J` is any bounded self-adjoint involution,

\[
J=J^*=J^{-1},
\tag{19}
\]

with no condition involving `D`, and assume

\[
-JF\succeq0.
\]

By (17), `J=KS` for some positive `K` commuting with `F`; hence it also commutes with `S=-sgn(F)`. Therefore

\[
I=J^2=K^2.
\tag{20}
\]

Since `K\succeq0`, the unique positive square root of the identity is the identity itself:

\[
K=I.
\tag{21}
\]

Consequently

\[
\boxed{
-JF\succeq0,
\quad
J=J^*=J^{-1}
\Longrightarrow
J=S=-\operatorname{sgn}(F).
}
\tag{22}
\]

Thus the parity-exchange assumption used in `WP-063` is not needed for uniqueness. **No other bounded fundamental symmetry can make the full-root channel positive.**

## 5. Nonunitary invertible metrics only reweight the absolute value

Suppose `J` is boundedly invertible and self-adjoint. From (17),

\[
J=KS
\]

with `K\succeq0`. Since `S` is unitary, invertibility of `J` is equivalent to invertibility of `K`. Therefore

\[
K\ge cI
\qquad
\text{for some }c>0.
\tag{23}
\]

The repaired form is simply

\[
-JF=K|F|.
\tag{24}
\]

Hence allowing a bounded nonunitary invertible metric enlarges the canonical repair only by a **positive commuting spectral weight**. It does not alter which spectral half is declared positive and cannot supply a sign theorem independent of `F`.

In particular, if `K=f(F)` is obtained by functional calculus, then

\[
J=-f(F)\operatorname{sgn}(F),
\qquad
-JF=f(F)|F|,
\tag{25}
\]

with `f\ge0`. The sign information is still exactly `sgn(F)`.

## 6. A positive Hilbert metric cannot repair the full channel without deleting half of it

A more conventional metric operator would itself be positive:

\[
J\succeq0.
\tag{26}
\]

Let `E_+` and `E_-` be the positive and negative spectral projections of `F`. `WP-062` proves that both spectral indices are infinite, so both subspaces are nonzero.

Under (17),

\[
J=-K\operatorname{sgn}(F).
\tag{27}
\]

On `E_+\mathcal H`,

\[
J=-K.
\tag{28}
\]

Since both `J` and `K` are positive, (28) forces

\[
K E_+=0,
\qquad
J E_+=0.
\tag{29}
\]

Therefore

\[
\boxed{
J\succeq0,
\quad
-JF\succeq0
\Longrightarrow
J\text{ annihilates the whole positive spectral subspace of }F.
}
\tag{30}
\]

In particular there is **no positive injective**, and hence no positive boundedly invertible, Hilbert metric that repairs `F` by left multiplication.

The same obstruction appears for a positive congruence. Let `G\succeq0` be bounded and injective. If

\[
G^{1/2}FG^{1/2}\succeq0,
\tag{31}
\]

then

\[
\langle Fy,y\rangle\ge0
\qquad
(y\in\operatorname{Ran}G^{1/2}).
\tag{32}
\]

The range of `G^{1/2}` is dense, so continuity would imply `F\succeq0`, contradicting the balanced indefiniteness of `WP-062`. Thus an ordinary positive change of Hilbert norm cannot turn this channel positive either.

## 7. Why the theorem is a no-go rather than a new positivity mechanism

Equation (17) might look like a large family of positive forms, because every positive commuting `K` gives

\[
-JF=K|F|\succeq0.
\]

But all of them are downstream of the same spectral sign. They do not prove that the signed full-root Hardy interaction was nonnegative; they replace it by a positively weighted absolute value.

This is exactly the issue already diagnosed concretely in `WP-063`: the indefinite even/odd interference

\[
-2\operatorname{Re}\int_0^1 a(t)\overline{b(t)}\,dt
\]

is converted into a positive sector norm. The present classification shows that **every bounded self-adjoint metric multiplication does the same thing in spectral coordinates**. Nonunitarity can change the positive weight `K`, but it cannot change the fact that the repair must know which spectral half of `F` is negative.

Therefore none of these bounded metric repairs supplies the missing independent geometric theorem required by the `weil_positivity` mandate. They also do not create the finite Mangoldt term, the Gamma extraction, or the polar counterterm as one coupled global form.

## 8. Matched control and prior-art audit

The classification in §2 contains no arithmetic. It holds for every bounded self-adjoint injective `A`. This is the strongest possible matched control: the sign mechanism survives after replacing the Hilbert block `H` by an arbitrary positive injective operator, exactly as the simpler control in `WP-063` already suggested.

The terminology is also classical. In Krein-space operator theory an operator `T` is called `J`-positive when `JT\ge0`; see, for example, Y. Xu, *J-Self-Adjoint Projections in Krein Spaces*, Journal of Function Spaces (2020), DOI `10.1155/2020/6725969`. Positive metric operators and bounded/unbounded metric changes are standard in the quasi-Hermitian literature; see J.-P. Antoine and C. Trapani, *Metric Operators, Generalized Hermiticity and Lattices of Hilbert Spaces*, arXiv:`1409.3497`. The spectral-sign/polar factor used here is standard bounded functional calculus.

No theorem-level novelty is claimed for those mechanisms. The Mathia-specific durable content is the exact scope statement obtained by applying them to the independently selected `q=2` channel: the bounded self-adjoint metric route left open in `WP-063` collapses completely to the polar sign already known to be insufficient.

## 9. Falsification surface

The claim has a short exact audit surface.

1. Check that `F` in (1) is bounded, self-adjoint, and injective.
2. From `-JF\succeq0`, verify that self-adjointness of the product forces `JF=FJ`.
3. Use the spectral theorem to verify that `J` then commutes with `|F|` and `sgn(F)`.
4. Put `K=-J sgn(F)` and verify `-JF=K|F|`.
5. Use the dense range of `|F|^{1/2}` to prove `K\succeq0`.
6. Verify the converse for every bounded positive `K` in the commutant of `F`.
7. Impose `J^2=I` and check that positivity of `K` forces `K=I`, yielding (22) without any `D`-odd hypothesis.
8. Impose `J\succeq0` and check that `J` must vanish on `E_+\mathcal H`.
9. Replace `F` by an arbitrary bounded self-adjoint injective control operator. The same proof must go through unchanged.

Any failure in steps 2–6 invalidates the classification. Success leaves only genuinely different escape routes: an **unbounded/domain-sensitive** metric, a non-multiplicative quotient or compression, or—most importantly for the branch mandate—a nonseparable finite-prime/archimedean/polar geometry in which the global coupling is constructed before the final sign theorem.

## Research consequence

`WP-063` left open “a larger nonunitary metric” as one possible way around the polar absolute-value obstruction. That statement can now be narrowed to

\[
\boxed{
\text{no bounded self-adjoint metric multiplication can escape the polar sign.}
}
\]

A successful Mathia-native positivity mechanism must therefore leave this bounded metric class. Merely replacing the canonical adjacent-parity involution by a bounded nonunitary self-adjoint metric cannot produce new arithmetic positivity; it can only reweight `|\mathcal F_2|` by a positive operator commuting with the same channel.
