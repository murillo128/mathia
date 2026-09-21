# PL-417 — The mod-5 supertrace has a canonical Pontryagin lift, but J-selfadjointness does not localize its spectrum

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-CLASSICALIZED`.

**Parent finding:** `PL-416`.

## Claim

`PL-416` leaves open an indefinite-space escape from its scalarization obstruction: retain the four mod-5 character channels and represent the repaired quadratic statistic in a Krein/Pontryagin space rather than forcing it into one positive Hilbert-space scalar variance. That representation exists canonically, but **indefinite selfadjointness alone supplies no Riemann-zero localization mechanism**.

The repaired character-space metric from `PL-416` is

\[
D=\operatorname{diag}(15,-1,-1,-1).
\]

Writing

\[
R=\operatorname{diag}(\sqrt{15},1,1,1),
\qquad
J=\operatorname{diag}(1,-1,-1,-1),
\]

one has the exact factorization

\[
\boxed{D=RJR.}
\tag{1}
\]

Hence for the four-channel vector `A`,

\[
A^*DA=(RA)^*J(RA).
\tag{2}
\]

So the unique mod-5 repair really does carry a natural Pontryagin signature `(1,3)` after a harmless positive diagonal rescaling. This is stronger than merely calling the statistic a signed sum: its finite local quadratic geometry has a canonical fundamental symmetry.

However, a `J`-selfadjoint operator need not have real spectrum. The exact `2 x 2` matrix

\[
J_2=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
T_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\tag{3}
\]

satisfies

\[
T_0^*J_2=J_2T_0
=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\tag{4}
\]

so `T_0` is `J_2`-selfadjoint, while

\[
\det(\lambda I-T_0)=\lambda^2+1,
\qquad
\sigma(T_0)=\{i,-i\}.
\tag{5}
\]

Embedding this block into the actual mod-5 signature,

\[
T=T_0\oplus a\oplus b,
\qquad a,b\in\mathbb R,
\tag{6}
\]

makes `T` `J`-selfadjoint for `J=diag(1,-1,-1,-1)` and leaves the nonreal pair `±i` in its spectrum. Therefore

\[
\boxed{
\text{mod-5 Pontryagin realization}
+J\text{-selfadjointness}
\not\Longrightarrow
\text{real spectrum}.
}
\tag{7}
\]

For an RH-facing construction this is decisive against the route **“preserve the PL-416 indefinite supertrace, construct a Krein/Pontryagin-selfadjoint operator, and infer critical-line localization from selfadjointness in that metric.”** The indefinite notion of selfadjointness permits precisely the kind of nonreal conjugate pair that a Hilbert–Pólya localization theorem would have to exclude.

The finding does **not** rule out Krein/Pontryagin methods. It identifies the missing theorem they must provide: an additional arithmetic property forcing real spectrum — for example `J`-nonnegativity, similarity to a Hilbert-space selfadjoint operator, a uniformly definite invariant spectral subspace, or another coercive structure strong enough to exclude every nonreal eigenvalue. Merely passing from the scalar Artin quotient of `PL-416` to an indefinite operator-valued realization is not enough.

## 1. The indefinite metric is intrinsic to the repaired mod-5 source

The exact source-side statistic isolated in `PL-415` and `PL-416`, after multiplying by `15`, has the form

\[
Q_5(X,L)=\sum_x A(x,L)^*D\,A(x,L),
\qquad
D=\operatorname{diag}(15,-1,-1,-1),
\tag{8}
\]

with channel vector

\[
A=(A_{\chi_0},A_{\chi_2},A_{\chi_4},A_{\bar\chi_4})^T.
\tag{9}
\]

The signature `(1,3)` is forced by the exact Fourier coefficients of the local inverse factor `g_5`; it is not introduced here to manufacture a counterexample. Equation (1) merely normalizes the positive coefficient `15` to `1`. Thus any exact finite-dimensional realization of (8) as a nondegenerate indefinite inner product is congruent to a form with one positive and three negative squares.

This matters because `PL-416` proved that a single scalar `L`-product can only produce a rank-one positive-semidefinite ordinary variance matrix `cc^*`, whereas the required quadratic observable has full rank and indefinite signature. A Pontryagin-space lift is therefore the most economical way to preserve exactly the information that scalarization destroys. The present finding tests that escape on its own terms rather than discarding the indefinite structure.

## 2. Indefinite selfadjointness is weaker than Hilbert selfadjointness in exactly the relevant way

For a fundamental symmetry `J=J^*=J^{-1}`, an operator `T` is `J`-selfadjoint when `JT` is selfadjoint in the underlying Hilbert inner product, equivalently

\[
T^*J=JT.
\tag{10}
\]

The witness (3)--(5) is the smallest possible obstruction. Its Hilbert adjoint is

\[
T_0^*=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]

and direct multiplication proves (4). Nevertheless `T_0` is a real rotation generator and has eigenvalues `±i`. No limiting argument, unbounded-domain subtlety, or analytic continuation is involved.

The same block embeds into the mod-5 signature because that form contains both a positive and a negative direction. Appending arbitrary real scalars on the two remaining negative coordinates preserves `J`-selfadjointness. Consequently the obstruction survives the exact finite signature supplied by the arithmetic decomposition; it is not a mismatch between an abstract Krein example and the local source geometry.

The general operator-theory statement is classical. Friedrich Philipp explicitly notes that, unlike Hilbert-space selfadjoint operators, `J`-selfadjoint operators need not have real spectrum and in general only have the corresponding conjugation symmetry; the same paper recalls that the stronger condition of `J`-nonnegativity, together with nonempty resolvent, gives real spectrum. Langer and Strauss likewise study `J`-selfadjoint block operator matrices in the presence of nonreal spectrum and derive additional sufficient hypotheses under which reality can be recovered. The novelty claim here is therefore **not** the Krein-space phenomenon. The line-specific delta is applying it to the exact `(1,3)` metric forced by `PL-416` and closing the previously open inference from indefinite realization alone to RH localization.

## 3. Definitizability does not repair the logical gap by itself

One might try to weaken the desired conclusion from ordinary Hilbert selfadjointness to a standard spectral class such as definitizable operators in a Krein/Pontryagin space. That still does not supply the required RH implication by itself. The point of definitizability is that the nonreal spectrum is highly controlled; it is not, in general, forced to be empty.

For this research line, a theorem allowing finitely many exceptional nonreal eigenvalues is qualitatively insufficient. RH is an **exception-free localization statement**. A construction that converts a hypothetical finite collection of off-critical zeros into finitely many nonreal eigenvalues remains compatible with the failure that must be ruled out. Thus an arithmetic argument must establish a condition that forces zero nonreal spectrum, not merely discreteness, finiteness, or conjugate pairing of the exceptional set.

This distinction parallels an earlier control in `PL-263`. There, creating a positive Hilbert metric by subtracting the least eigenvalue makes a generalized Weil pencil real even for explicitly off-line input, so spectral reality after manufactured positivity is not RH-sensitive. Here the complementary shortcut also fails: **preserving an indefinite metric and calling the resulting operator selfadjoint in that metric does not make its spectrum real in the first place.** Between the two findings, neither positivity manufactured after the fact nor indefinite selfadjointness without an extra sign theorem supplies the missing localization mechanism.

## 4. Relation to the Riemann-zero symmetry

The counterexample is intentionally structural rather than a claim that the matrix `T_0` models zeta zeros. A hypothetical off-critical Riemann zero is accompanied by its functional-equation/conjugation partners. In the usual spectral coordinate centered at `1/2`, an off-line pair appears as nonreal conjugate spectral parameters. Generic `J`-selfadjointness is compatible with such conjugate symmetry; it does not collapse the pair to the real axis.

Therefore the symmetry furnished automatically by indefinite selfadjointness is of the wrong logical strength. It can reproduce a necessary symmetry pattern of the completed zeta divisor while leaving the horizontal displacement from the critical line unconstrained. Any proposed mod-5 operator must expose an additional arithmetic order/positivity law whose failure can actually distinguish an off-line control from an on-line one.

A particularly clean surviving target is to derive, rather than assume, a relation of the form

\[
JT\ge 0
\tag{11}
\]

for an operator `T` whose spectral parameter genuinely corresponds to the zeta-zero coordinate. Standard Krein theory then gives real spectrum under appropriate closedness/resolvent hypotheses. But (11) would be a new arithmetic coercivity theorem; it does not follow from the source identity (8), from the virtual-character factorization, or from `J`-selfadjointness. In fact the signed weights in `D` make such positivity exactly the sort of nontrivial cancellation statement the line has repeatedly found to be missing.

Other routes — similarity to a Hilbert-space selfadjoint operator, a positive metric operator intertwined with the character dynamics, or a definiteness theorem on the actual invariant spectral subspace — face the same gate: the property enforcing reality must be proved from the rational-prime source and must fail under a matched off-line control. Otherwise it is only a choice of representation.

## 5. Prior-art and adversarial audit

The exact arithmetic input is the already-audited `PL-416` identity. The finite-dimensional factorization `D=RJR` and witness (3)--(6) are elementary exact derivations. They were checked directly: `T_0^*J_2=J_2T_0`, and the characteristic polynomial is `lambda^2+1`; for `T=T_0 direct-sum a direct-sum b`, the characteristic polynomial is `(lambda^2+1)(lambda-a)(lambda-b)`.

The closest operator-theory prior art confirms that the obstruction is standard rather than a new Krein theorem:

- Friedrich Philipp, **“Relatively Bounded Perturbations of J-Non-Negative Operators,”** *Complex Analysis and Operator Theory* **17** (2023), Article 14, DOI `10.1007/s11785-022-01263-2`. The introduction states the general failure of spectral reality for `J`-selfadjoint operators and contrasts it with the real-spectrum property of `J`-nonnegative operators.
- Matthias Langer and Michael Strauss, **“Spectral properties of unbounded J-self-adjoint block operator matrices,”** *Journal of Spectral Theory* **7**(1) (2017), 137–190, DOI `10.4171/JST/158`. The paper treats nonreal spectrum as an admissible feature of `J`-selfadjoint block operators and supplies additional sufficient conditions for spectral reality.

The decisive adversarial checks are as follows. The nonreal witness uses the exact positive/negative signature already present in the mod-5 metric, so it cannot be dismissed as requiring a different indefinite index. Rescaling the `15` coefficient changes only `R` and not the fundamental signature. Appending the remaining two negative directions cannot remove the nonreal block. Conversely, no claim is made that every `J`-selfadjoint realization has nonreal spectrum; many have real spectrum. The obstruction is to **automatic** localization from the indefinite selfadjointness axiom alone.

Nor is the claim that no Krein-space construction can prove RH. A successful one could do so only by proving an extra property that is itself RH-sensitive. The present result therefore closes one representation shortcut while preserving a precise falsifiable frontier.

## Consequence for the research line

`PL-416` showed that the repaired mod-5 variance cannot be compressed faithfully into one scalar Artin `L`-function at quadratic order and suggested that an indefinite block/super-Hilbert realization might preserve the necessary channel data. The current result says exactly what that suggestion can and cannot buy.

The **representation problem is solved locally**: the source supertrace has the canonical Pontryagin metric (1). The **localization problem is not**: `J`-selfadjointness permits nonreal pairs even in the same signature. Therefore future work should not spend passes on constructing an indefinite metric merely to regain a word such as “selfadjoint.” The next admissible mechanism must derive an arithmetic condition that is stronger than indefinite selfadjointness and that forces the relevant spectrum to be real without first erasing the signed mod-5 source information.

The clean falsification gate is:

\[
\boxed{
\text{if a proposed Krein/Pontryagin mechanism still admits the embedded block }T_0,
\text{ it cannot by itself localize zeta zeros.}
}
\tag{12}
\]

Equivalently, a surviving proposal must identify the exact additional hypothesis that excludes (3), prove that hypothesis from the prime-side construction, and verify that it is not a generic consequence of choosing a convenient indefinite representation.