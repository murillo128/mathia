# AF-091 — Ultrasummand kernels close the nonseparable Lipschitz-lifting escape

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
0\longrightarrow K\xrightarrow{i}E\xrightarrow{q}F\longrightarrow0
\tag{1}
\]

be a short exact sequence of real or complex Banach spaces, with `q` a bounded linear surjection. Suppose that on one nontrivial ball of `F` there is an `L`-Lipschitz right inverse

\[
s:y_0+rB_F\to E,
\qquad
q s(y)=y.
\tag{2}
\]

Assume in addition that the kernel `K` is an **ultrasummand**: its canonical copy `J_K(K)` is complemented in `K^{**}`. Then the original sequence (1) splits linearly. Equivalently, `K` is complemented in `E`, and `q` has a bounded linear right inverse

\[
V:F\to E,
\qquad qV=I_F.
\tag{3}
\]

Thus the nonseparable Lipschitz-but-not-linear escape left open by AF-082 and AF-090 can occur only when the kernel itself fails this bidual-complementability gate.

More quantitatively, suppose

\[
\Pi:K^{**}\to J_K(K)
\tag{4}
\]

is a projection with `||Pi||<=beta`. AF-087 yields a global right inverse `H:F->E` with

\[
\operatorname{Lip}(H)\le 3L.
\tag{5}
\]

Then there is a bounded linear projection

\[
P:E\to K
\tag{6}
\]

with

\[
\boxed{
\|P\|
\le
\beta\bigl(1+3L\|q\|\bigr).
}
\tag{7}
\]

If `F=E/K` carries the canonical quotient norm and `q:E->E/K` is the canonical quotient map, one may choose a bounded linear section satisfying

\[
\boxed{
\|V\|
\le
1+\beta(1+3L).
}
\tag{8}
\]

No sharpness is claimed for these constants; the factor `3` is inherited from AF-087's elementary conical globalization.

The structural consequence is the important part:

\[
\boxed{
\begin{array}{c}
\text{local neighborhood-Lipschitz quotient repair}\\[2mm]
+\ \text{kernel complemented in its bidual}
\end{array}
\Longrightarrow
\text{original-space linear splitting}.}
\tag{9}
\]

Together with AF-082, this gives two independent closure gates for a genuinely nonlinear Lipschitz lifting:

\[
\boxed{
\text{Lipschitz but not linear}
\Longrightarrow
\begin{cases}
F\text{ is nonseparable},\\
K\text{ is not an ultrasummand}.
\end{cases}}
\tag{10}
\]

The classical Aharoni--Lindenstrauss phenomenon evades both gates: its relevant quotient is nonseparable and its kernel is `c_0`, which is not complemented in `c_0^{**}=\ell_\infty`.

## Derivation

### 1. The local patch gives a global Lipschitz retract onto the kernel

AF-087 converts (2) into a global right inverse

\[
H:F\to E,
\qquad
qH=I_F,
\qquad
H(0)=0,
\qquad
\operatorname{Lip}(H)\le3L.
\tag{11}
\]

Define

\[
R:E\to K,
\qquad
R(x):=x-H(qx).
\tag{12}
\]

Then `qR(x)=0`, and if `k in K` then `R(k)=k`. Hence `R` is a Lipschitz retraction of `E` onto `K`. Its Lipschitz constant obeys

\[
\operatorname{Lip}(R)
\le
1+\|q\|\operatorname{Lip}(H)
\le
1+3L\|q\|.
\tag{13}
\]

This is the bridge from the local recovery hypothesis to classical local-complementation theory.

### 2. A Lipschitz retract gives a bounded linear extension operator on the dual

Kalton's Proposition 3.21 states that a linear subspace which is a Lipschitz retract of a Banach space is locally complemented. Its proof gives the form needed here.

There exists a bounded linear extension operator

\[
U:K^*\to E^*,
\qquad
i^*U=I_{K^*},
\tag{14}
\]

and the construction through the norm-one projection from `Lip_0(E)` onto `E^*` gives

\[
\|U\|
\le
\operatorname{Lip}(R)
\le
1+3L\|q\|.
\tag{15}
\]

Taking adjoints,

\[
U^*:E^{**}\to K^{**}.
\tag{16}
\]

For every `k in K`, the extension identity in (14) implies

\[
U^*J_E i(k)=J_K(k).
\tag{17}
\]

Thus `U^*` already recovers the correct kernel point after passing to the bidual; what is missing is a controlled way to return from `K^{**}` to `K`.

### 3. Kernel bidual complementability performs exactly that descent

Let `Pi` be as in (4), and identify `J_K(K)` with `K`. Define

\[
P
:=
J_K^{-1}\Pi U^*J_E:E\to K.
\tag{18}
\]

This map is bounded and linear. By (17), for `k in K`,

\[
P(i(k))
=J_K^{-1}\Pi J_K(k)
=k.
\tag{19}
\]

Hence `P` is a bounded linear projection of `E` onto `K`. Moreover,

\[
\|P\|
\le
\|\Pi\|\,\|U\|
\le
\beta(1+3L\|q\|),
\tag{20}
\]

which proves (7).

This is the elementary dual/bidual mechanism behind the standard homological statement that a **locally split** exact sequence whose kernel is an ultrasummand actually splits.

### 4. A projection onto the kernel gives a linear quotient section

For the canonical quotient `Q:E->E/K`, define

\[
V(Qx):=(I_E-iP)x.
\tag{21}
\]

This is well defined: if `Qx=Qx'`, then `x-x' in K`, and `(I-iP)(x-x')=0`. It is linear and

\[
QV(Qx)=Qx.
\tag{22}
\]

For every `epsilon>0`, choose a representative `x` of `y in E/K` with

\[
\|x\|\le\|y\|+\epsilon.
\tag{23}
\]

Then

\[
\|Vy\|
\le
\|I-iP\|\,\|x\|,
\tag{24}
\]

so, letting `epsilon downarrow0`,

\[
\|V\|
\le
\|I-iP\|
\le
1+\|P\|.
\tag{25}
\]

Combining (20) and (25) gives (8). For a general bounded surjection `q:E->F`, the induced Banach-space isomorphism `E/K -> F` transfers this section to (3); the quantitative bound additionally carries the norm of the inverse quotient identification.

## Exact controls

### Reflexive-kernel control

If `K` is reflexive, `K=K^{**}` canonically, so the ultrasummand gate is automatic with `beta=1`. Therefore **a nonseparable quotient target does not by itself permit nonlinear Lipschitz lifting**: if the kernel is reflexive, one neighborhood-Lipschitz section already forces a bounded linear section of the original quotient.

This is complementary to AF-082. AF-082 closes the escape from the **target side** by assuming `F` separable; AF-091 closes it from the **kernel side** by assuming `K` complemented in its bidual.

### Dual and L-embedded kernel controls

Every dual Banach space is canonically norm-one complemented in its bidual, and classical L-embedded spaces carry a norm-one projection from their bidual onto the original space. Whenever such a space occurs as the kernel, the same conclusion follows with `beta=1`.

The claim does not require the projection `Pi` to interact with `E` or `q` beforehand. The local-complementation extension `U` in (14) supplies the compatibility needed to compose `E -> E^{**} -> K^{**} -> K`.

### Aharoni--Lindenstrauss matched escape

The classical nonseparable Aharoni--Lindenstrauss construction used in AF-090 produces a quotient with a Lipschitz lifting but no bounded linear lifting. In the standard realization inherited from

\[
\ell_\infty\to\ell_\infty/c_0,
\tag{26}
\]

the restricted quotient retains kernel `c_0`. Since `c_0` is not complemented in `\ell_\infty=c_0^{**}`, `c_0` is not an ultrasummand.

Thus the standard counterexample does not contradict (9); it realizes exactly the missing kernel-side hypothesis. Combined with its nonseparable target, it also shows that both conditions in the necessary double escape (10) are genuinely inhabited by known nonlinear lifting phenomena.

### Split-sequence control

The ultrasummand condition is **not necessary** for a particular quotient to split. If (1) already has a bounded linear section, then `K` is complemented in `E` regardless of whether `K` is complemented in `K^{**}`.

Accordingly, AF-091 gives a sufficient structural closure gate and a necessary condition for a Lipschitz-but-not-linear counterexample; it is not a characterization of all split quotients.

## Prior art and novelty assessment

The theorem-level Banach-space ingredients are classical, and **no novelty is claimed** for the implication itself.

- Nigel J. Kalton, **“The nonlinear geometry of Banach spaces,”** *Revista Matemática Complutense* 21(1) (2008), 7--60, DOI `10.5209/rev_REMA.2008.v21.n1.16426`. Proposition 3.21 proves that a linear subspace which is a Lipschitz retract is locally complemented; its proof explicitly constructs the dual extension operator used in (14).
- Félix Cabello Sánchez and Jesús M. F. Castillo, **“Local Methods in the Theory of Twisted Sums,”** in *Homological Methods in Banach Space Theory*, Cambridge University Press (2023), Chapter 5, DOI `10.1017/9781108778312.007`. The standard local-splitting theory developed there includes the result that a locally split exact sequence whose kernel is an ultrasummand splits. A 2026 paper of Castillo and Moreno explicitly invokes this as Proposition 5.1.6 of the monograph.
- Israel Aharoni and Joram Lindenstrauss, **“Uniform equivalence between Banach spaces,”** *Bulletin of the American Mathematical Society* 84(2) (1978), 281--283, DOI `10.1090/S0002-9904-1978-14475-9`. Their nonseparable Lipschitz/nonlinear phenomenon supplies the matched escape boundary.
- AF-087 and AF-090 supply the Mathia-local bridge: one local Lipschitz patch globalizes to a Lipschitz section/retraction, and therefore forces local complementation and bidual linear splitting.

A targeted audit of locally split exact sequences, ultrasummands, Lipschitz retracts, and subspace-respecting lifting theory confirms that the central implication is established classical Banach homology rather than a new theorem. The durable Arithmetic Fidelity value is the **placement of this classical closure theorem at the exact remaining AF-090 boundary** and the resulting two-sided exclusion (10): a genuinely nonlinear stable quotient repair must simultaneously evade target-side separable linearization and kernel-side bidual descent.

Subspace-respecting local-reflexivity and lifting theories, including Eve Oja's principle of local reflexivity respecting subspaces and Chávez-Domínguez's Ando--Choi--Effros lifting theorem respecting subspaces, provide adjacent language for compatibility constraints but are not needed for the proof above.

## Boundaries and failure modes

- The conclusion uses neighborhood **Lipschitz** repair. Pointwise Lipschitz regularity, Hölder repair, bounded-ball uniform continuity, or tangent-direction control remain weaker categories and are not covered.
- The argument does not prove the converse “locally complemented implies Lipschitz retract.” Kalton's survey identifies that converse as tied to the separate and difficult problem of Lipschitz retractions from biduals.
- The ultrasummand hypothesis is imposed on the **kernel** `K`, not on the quotient `F` or the source `E`. Moving the hypothesis to a different term of the exact sequence requires a separate theorem.
- The quantitative constants in (7)--(8) are not claimed optimal. A sharper local-to-global Lipschitz constant than AF-087's `3` would improve them automatically.
- Complementability of `K` in `K^{**}` is sufficient for descent from local linear structure to an original-space projection. Failure of that complementability does not imply that a Lipschitz lifting without a linear lifting exists.
- The statement concerns complete representative recovery for linear quotients. Discriminator-specific recovery may require much less than a full right inverse and can escape these exact-sequence gates.
- No rational-prime or RH conclusion follows directly. The reusable lesson is categorical: **stable quotient repair can remain genuinely nonlinear only when the destination and the forgotten fiber both evade classical linearization mechanisms.**