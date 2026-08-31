# WP-063 — the `q=2` Hardy Krein repair is uniquely the polar absolute value

**Status:** `EXACT-DERIVED + DECISIVE-BOUNDARY + CLASSICAL-MECHANISM + PRIOR-ART-REDIRECTION`. The polar-decomposition and fundamental-symmetry ingredients are classical operator/Krein-space mechanisms. The durable Mathia-specific result is an exact classification of the symmetry-breaking route left open by `WP-062`: once the full-root `q=2` Hardy channel is required to be made positive by a self-adjoint unitary metric that exchanges the canonical even/odd sectors, positivity forces a unique metric. That metric is exactly minus the spectral sign of the channel, and the repaired positive operator is exactly its absolute value. Thus the natural `D`-odd Krein/fundamental-symmetry route does not supply an independent new sign theorem beyond the polar absolute-value repair already identified as insufficient in `WP-061`.

The result does **not** rule out a larger nonunitary metric, a non-`D`-odd polarization forced by additional geometry, or a genuinely nonseparable finite–archimedean–polar construction. It rules out treating an arbitrary parity-exchanging fundamental symmetry as a new source of positivity: within that entire class there is only the polar sign.

## 1. The full-root `q=2` channel is an exact off-diagonal Hilbert operator

`WP-061` and `WP-062` identify the Hardy operator of the canonically selected full-root field

\[
V_2(z)=\Log(1-z^2)
\]

as

\[
\mathcal F_2=-H+DHD,
\qquad
H_{jk}=\frac1{j+k+1},
\qquad
De_j=(-1)^j e_j.
\tag{1}
\]

Split the Hardy basis into even and odd indices and reindex each sector by

\[
e_{2j}\longleftrightarrow (e_j,0),
\qquad
e_{2j+1}\longleftrightarrow(0,e_j).
\tag{2}
\]

The same-parity matrix entries of `F_2` vanish, while for one even and one odd index

\[
-2H_{2i,2j+1}
=
-\frac{2}{2i+2j+2}
=
-\frac1{i+j+1}.
\tag{3}
\]

Therefore the full operator is exactly

\[
\boxed{
\mathcal F_2
=
\begin{pmatrix}
0&-H\\
-H&0
\end{pmatrix}
}
\tag{4}
\]

on `ell^2 ⊕ ell^2`, with

\[
D=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix}.
\tag{5}
\]

This is stronger than merely knowing the chiral relation `D F_2 D=-F_2`: the off-diagonal block is again the **same classical Hilbert matrix** that generated the primitive positive `q=2` shell in `WP-061`.

The Hilbert matrix is a bounded positive injective operator. Positivity follows from its moment realization

\[
\langle a,Ha\rangle
=
\int_0^1
\left|\sum_{j\ge0}a_jt^j\right|^2dt
\ge0,
\tag{6}
\]

and injectivity follows because a Hardy power series that vanishes almost everywhere on an interval vanishes identically. Since `H=H*` and `ker H=0`,

\[
\overline{\operatorname{Ran}H}
=
(\ker H)^\perp
=
\ell^2.
\tag{7}
\]

The dense-range fact will make the positivity repair unique.

## 2. A canonical adjacent-parity involution makes the channel positive

Let `V` be the unilateral Hardy shift,

\[
Ve_j=e_{j+1},
\tag{8}
\]

and let

\[
Q_{\rm e}=\frac{I+D}{2},
\qquad
Q_{\rm o}=\frac{I-D}{2}
\tag{9}
\]

be the parity projections. There is a natural self-adjoint unitary involution pairing adjacent even and odd monomials,

\[
\boxed{
S
=
Q_{\rm o}VQ_{\rm e}
+
Q_{\rm e}V^*Q_{\rm o}.
}
\tag{10}
\]

Explicitly,

\[
Se_{2j}=e_{2j+1},
\qquad
Se_{2j+1}=e_{2j},
\tag{11}
\]

so in the decomposition (2),

\[
S=
\begin{pmatrix}
0&I\\
I&0
\end{pmatrix},
\qquad
S=S^*=S^{-1},
\qquad
SD=-DS.
\tag{12}
\]

Multiplying (4) gives the exact positive repair

\[
\boxed{
-S\mathcal F_2
=
\begin{pmatrix}
H&0\\
0&H
\end{pmatrix}
\succeq0.
}
\tag{13}
\]

This is a genuine positivity theorem on the full-root channel, and `S` can be written using the pre-existing Hardy shift and parity without first diagonalizing `F_2`. That prevents a too-quick dismissal of the construction as merely “choose the positive spectral subspace”.

However, the next step shows that this apparent escape is exactly polar decomposition in disguise.

## 3. The repaired operator is exactly `|F_2|`, and `S` is exactly its spectral sign

Put

\[
A=
\begin{pmatrix}
H&0\\
0&H
\end{pmatrix}.
\tag{14}
\]

Equation (4) is

\[
\mathcal F_2=-SA.
\tag{15}
\]

The operators `S` and `A` commute, so

\[
\mathcal F_2^2=A^2.
\tag{16}
\]

Since `A` is positive,

\[
\boxed{
|\mathcal F_2|
=
(\mathcal F_2^2)^{1/2}
=
A
=
\begin{pmatrix}
H&0\\
0&H
\end{pmatrix}.
}
\tag{17}
\]

Combining (13) and (17),

\[
\boxed{
-S\mathcal F_2
=
|\mathcal F_2|.
}
\tag{18}
\]

Because `H` is injective, so is `F_2`; hence its polar partial isometry is a unitary involution. On the dense range of `|F_2|=A`,

\[
\mathcal F_2
=
(-S)|\mathcal F_2|.
\tag{19}
\]

By uniqueness of the polar factor,

\[
\boxed{
\operatorname{sgn}(\mathcal F_2)=-S.
}
\tag{20}
\]

Thus the adjacent-parity involution is not an additional positive geometry sitting alongside the full-root channel. It is precisely the sign operator that converts that channel to its absolute value.

## 4. Positivity uniquely forces this polar metric among all `D`-odd fundamental symmetries

The preceding identity could still leave open many other parity-breaking Krein metrics. There are none in the natural unitary class.

Let

\[
J=J^*=J^{-1}
\tag{21}
\]

be an arbitrary bounded fundamental symmetry satisfying

\[
JD=-DJ.
\tag{22}
\]

Relative to the even/odd decomposition, anticommutation with `D` forces `J` to be off diagonal. Self-adjoint unitarity then gives

\[
\boxed{
J=
\begin{pmatrix}
0&U^*\\
U&0
\end{pmatrix}
}
\tag{23}
\]

for a unitary `U` on `ell^2`.

Using (4),

\[
-J\mathcal F_2
=
\begin{pmatrix}
U^*H&0\\
0&UH
\end{pmatrix}.
\tag{24}
\]

Assume this is positive semidefinite. Then in particular

\[
B:=U^*H\succeq0.
\tag{25}
\]

But

\[
H=UB.
\tag{26}
\]

Taking adjoint products,

\[
H^2
=
(UB)^*(UB)
=
B^2.
\tag{27}
\]

Both `H` and `B` are positive, so uniqueness of the positive square root gives

\[
B=H.
\tag{28}
\]

Equation (26) becomes

\[
UH=H.
\tag{29}
\]

Since `Ran H` is dense and `U` is bounded,

\[
U=I.
\tag{30}
\]

Therefore

\[
\boxed{
-J\mathcal F_2\succeq0
\quad\Longrightarrow\quad
J=S.
}
\tag{31}
\]

Changing the sign gives the companion statement

\[
\boxed{
J\mathcal F_2\succeq0
\quad\Longrightarrow\quad
J=-S.
}
\tag{32}
\]

So the entire class of self-adjoint unitary parity-exchanging metrics collapses to the two polar choices. Positivity does not merely *permit* the absolute-value repair; it **forces** it.

## 5. The moment picture shows exactly what the repair discards

For a finitely supported Hardy coefficient vector `c`, write its even and odd parts as

\[
a_j=c_{2j},
\qquad
b_j=c_{2j+1},
\tag{33}
\]

with generating functions

\[
a(t)=\sum_{j\ge0}a_jt^j,
\qquad
b(t)=\sum_{j\ge0}b_jt^j.
\tag{34}
\]

The full-root indefinite form from `WP-062` can then be rewritten using (4) and the Hilbert moment formula as

\[
\boxed{
\langle c,\mathcal F_2c\rangle
=
-2\operatorname{Re}
\int_0^1
a(t)\overline{b(t)}\,dt.
}
\tag{35}
\]

This is exactly the **interference term** between the even and odd Hardy sectors.

By contrast, the unique positive `D`-odd repair is

\[
\boxed{
\langle c,|\mathcal F_2|c\rangle
=
\int_0^1
\left(
|a(t)|^2+|b(t)|^2
\right)\,dt
\ge0.
}
\tag{36}
\]

Thus the polar repair does not prove that the signed interference was secretly nonnegative. It replaces that interference by the sum of the two sector norms. This makes the information loss completely explicit.

It also clarifies why the result does not contradict `WP-036`. The positive-real radial Mellin response there is built from a **Dirichlet Gram family** and is already quadratic in the radial fields. Changing a Hardy field by a sign does not imply a corresponding sign change in that Gram response. The present theorem is narrower: it classifies positive fundamental-symmetry repairs of the *linear full-root Hardy operator* `F_2`.

## 6. Matched control: the sign theorem is universal chiral polar algebra

The same construction works with no arithmetic at all. Let `P` be any bounded positive injective operator on a Hilbert space and define

\[
F_P=
\begin{pmatrix}
0&-P\\
-P&0
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&I\\
I&0
\end{pmatrix}.
\tag{37}
\]

Then

\[
-SF_P=P\oplus P=|F_P|,
\qquad
\operatorname{sgn}(F_P)=-S.
\tag{38}
\]

The proof of the uniqueness implication (31) is unchanged whenever `P` has dense range, which injectivity supplies for self-adjoint `P`.

Therefore neither the existence nor the uniqueness of the positive metric is RH-specific. The arithmetic information of Prime Circle remains in how its particular operator was constructed and how it couples to other shell data, not in this positivity theorem.

This matched control is decisive for the novelty audit. Fundamental symmetries in indefinite inner-product spaces and polar decomposition/sign operators are standard operator theory. The Mathia-specific contribution is the exact identification

\[
\boxed{
\text{canonical `q=2` parity swap}
=
-\operatorname{sgn}(\mathcal F_2),
}
\tag{39}
\]

together with the uniqueness theorem (31) for the route opened by `WP-062`. No historical novelty is claimed for the general mechanism.

## 7. Why this still does not yield the completed Weil form

The repaired operator is the universal positive block

\[
|\mathcal F_2|=H\oplus H.
\tag{40}
\]

No identity currently identifies this operator with the completed Weil quadratic form. In particular:

- `WP-061` shows that the direct positive `q=2` Hardy Gram gives nonzero shell energy on every separated shell rather than the sparse Mangoldt support.
- `WP-036`/`WP-048` obtain the Riemann Gamma logarithmic derivative from a radial Mellin **Gram response** only after an affine extraction; equation (40) is not that extraction.
- the finite term required by the Weil formula remains the signed sparse birth/resultant data, and the polar counterterm is still absent from (40).
- the positive theorem (38) survives arbitrary non-arithmetic choices of `P`, so it cannot by itself distinguish the Riemann arithmetic from matched controls.

Consequently it would be circular to argue that (13) has solved the sign problem merely because `S` has an independent Hardy-shift formula. The independent formula makes `S` a legitimate candidate to test; equations (17)--(31) show what the test reveals: **within the whole `D`-odd unitary metric class, its positivity is exactly the absolute-value mechanism and nothing stronger.**

## 8. Falsification surface and research consequence

The claim has short exact audit points.

1. Reindex the even/odd Hardy sectors and verify the exact block identity (4).
2. Verify the shift formula (10), `S^2=I`, and `SD=-DS`.
3. Multiply the blocks to obtain (13).
4. Verify `F_2^2=diag(H^2,H^2)` and hence (17).
5. Use injectivity of the Hilbert matrix to conclude dense range and the polar-sign identity (20).
6. Classify every self-adjoint unitary anticommuting with `D` as (23).
7. Under the hypothesis `-J F_2 >= 0`, derive `B=U^*H>=0`, then `H=UB`, `H^2=B^2`, `B=H`, and finally `U=I`.
8. Run the generic positive-operator control (37)--(38). Success confirms that the positivity theorem is universal rather than arithmetic.

Failure of any of items 1--7 invalidates the uniqueness obstruction. Their success still leaves materially different routes open: nonunitary or unbounded metrics, a polarization not constrained to anticommute with `D`, quotients/compressions using additional Mathia geometry, and most importantly a nonseparable construction in which finite-prime, `q=2` archimedean, and polar sectors are coupled **before** the final sign theorem.

The branch can therefore be narrowed from

\[
\text{“find a canonical parity-breaking positive metric for }\mathcal F_2\text{”}
\]

to

\[
\boxed{
\text{“a successful completion must add structure beyond a `D`-odd fundamental symmetry,}
\quad
\text{because that class uniquely returns }|\mathcal F_2|.”}
\]

That is the decisive boundary established here.
