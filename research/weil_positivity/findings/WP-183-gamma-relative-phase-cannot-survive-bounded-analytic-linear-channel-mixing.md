# WP-183 — The Gamma relative phase cannot survive bounded analytic linear channel completion after quotienting

**Status:** `EXACT-DERIVED + H-INFINITY-ZERO-DIVISOR + STABLE-CHANNEL-NO-GO + PYTHAGOREAN-COMPLETION-BOUNDARY + MATCHED-INNER-CONTROL + DECISIVE-NARROWING + NOT-WEIL-POSITIVITY`.

`WP-169` isolates the exact real-place relative phase

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})},
\qquad |R_\infty(\tau)|=1
\quad(\tau\in\mathbb R),
\tag{1}
\]

between the Mathia pointed-shell scaling factor and its Nyman comparator. `WP-170` proves that the upper-half-plane continuation of `R_infty` is not Schur/inner because its zeros

\[
z_n=i\left(2n+\frac12\right),\qquad n\ge0,
\tag{2}
\]

violate the Blaschke condition. `WP-182`, on a different branch of the same boundary-response search, shows that a genuinely dissipative **Schur** response can nevertheless admit a canonical positive Pythagorean/Darlington defect completion: the scalar signed phase may live inside a larger positive two-channel kernel.

A natural attempt to join those two facts is to start from the normalized phase pair `(1,R_infty)`, apply a bounded analytic linear channel mixer to obtain a dissipative Schur component and its companion channel, and then invoke the positive completion mechanism of `WP-182`.

That bridge is impossible in a stronger sense than ordinary passivity failure. The non-Blaschke divisor of `R_infty` makes it impossible for **any bounded analytic linear channelization** to retain a nonzero `R_infty` component while producing bounded analytic outputs. No contractivity, positivity, finite-dimensionality, rationality, or invertibility assumption on the mixer is needed.

Precisely, if `a,b` are bounded analytic functions on the upper half-plane and

\[
f=a+bR_\infty
\tag{3}
\]

is also bounded analytic, then necessarily

\[
\boxed{b\equiv0.}
\tag{4}
\]

Equivalently,

\[
\boxed{
m\in H^\infty,\quad mR_\infty\in H^\infty
\Longrightarrow m\equiv0.
}
\tag{5}
\]

The same statement holds coefficientwise for matrix- or operator-valued bounded analytic mixers. Therefore a bounded analytic column-inner/Pythagorean completion cannot be manufactured from `(1,R_infty)` by any stable linear filter bank unless it erases the Gamma phase completely.

This does **not** rule out a source-derived coupled object formed before the quotient in `WP-169`, nor a singular/meromorphic or nonlinear category change. It rules out a particularly natural post-quotient repair: the exact Gamma phase cannot first be isolated and then regularized into the `WP-182` positive Schur geometry by bounded analytic linear mixing.

## 1. The non-Blaschke divisor is inherited by every bounded multiplier

Work on the upper half-plane

\[
\mathbb H=\{z:\operatorname{Im}z>0\}.
\]

The continuation of (1) used in `WP-170` is analytic on `H`. Its zero sequence is exactly (2). Put

\[
y_n=2n+\frac12.
\]

Then

\[
\sum_{n\ge0}
\frac{\operatorname{Im}z_n}{1+|z_n|^2}
=
\sum_{n\ge0}\frac{y_n}{1+y_n^2}
=\infty,
\tag{6}
\]

because the summand is asymptotic to `1/(2n)`.

Every nonzero `H^infinity(H)` function has a zero divisor satisfying the upper-half-plane Blaschke condition. This is the standard zero-set theorem already used in `WP-170`.

Now let

\[
m\in H^\infty(\mathbb H)
\tag{7}
\]

and suppose `m R_infty` is also in `H^infinity(H)`. If `m` were not identically zero, then `mR_infty` would be a nonzero bounded analytic function. But every `z_n` is still a zero of the product: multiplication by an analytic function can add zero multiplicity but cannot cancel a zero of `R_infty`. Hence the zero divisor of `mR_infty` contains the divergent subsequence (2), contradicting (6).

Therefore

\[
\boxed{mR_\infty\in H^\infty(\mathbb H),\ m\in H^\infty(\mathbb H)
\Longrightarrow m\equiv0.}
\tag{8}
\]

This is stronger than saying that a constant attenuation `rho R_infty`, `0<rho<1`, is not Schur. No nonzero bounded analytic attenuation can regularize the exact phase into **any bounded analytic function at all**. The obstruction is its inherited zero divisor, not its boundary norm.

## 2. Every bounded analytic affine channel readout erases the phase

Let

\[
a,b\in H^\infty(\mathbb H)
\tag{9}
\]

and suppose

\[
f=a+bR_\infty\in H^\infty(\mathbb H).
\tag{10}
\]

Then

\[
bR_\infty=f-a\in H^\infty(\mathbb H).
\tag{11}
\]

Applying (8) gives `b=0`, proving (4).

Thus the two-dimensional source vector

\[
v(z)=\binom{1}{R_\infty(z)}
\tag{12}
\]

has a sharp bounded-channel property. If

\[
M(z)=
\begin{pmatrix}
a_1(z)&b_1(z)\\
\vdots&\vdots\\
a_d(z)&b_d(z)
\end{pmatrix},
\qquad
M_{jk}\in H^\infty(\mathbb H),
\tag{13}
\]

and

\[
F(z)=M(z)v(z)
\tag{14}
\]

has bounded analytic components, then (4) applied row by row gives

\[
\boxed{b_j\equiv0\quad\text{for every }j.}
\tag{15}
\]

So every such bounded analytic output factors through the projection onto the constant channel. The `R_infty` channel is not merely hard to make contractive; it is completely invisible to bounded analytic **linear** output maps.

The statement is dimension independent. Let `A(z),B(z)` be bounded analytic operator-valued functions between Hilbert spaces and assume

\[
G(z)=A(z)+R_\infty(z)B(z)
\tag{16}
\]

is bounded analytic. For fixed vectors `u,v`, each scalar matrix coefficient satisfies

\[
\langle u,G(z)v\rangle
=
\langle u,A(z)v\rangle
+R_\infty(z)\langle u,B(z)v\rangle.
\tag{17}
\]

Equation (4) forces every coefficient of `B` to vanish, hence

\[
\boxed{B\equiv0.}
\tag{18}
\]

Infinite channel dimension therefore does not help as long as the channel transformation itself is a bounded analytic linear map and the visible output remains bounded analytic.

## 3. Consequence for the Pythagorean escape of WP-182

The positive completion in `WP-182` starts with a non-extreme scalar Schur function `S` and its outer Pythagorean mate `A`, producing a bounded analytic column

\[
F=\binom{S}{A}
\tag{19}
\]

with boundary identity

\[
|S|^2+|A|^2=1
\tag{20}
\]

and a positive de Branges--Rovnyak kernel for the completed channel.

Suppose one tries to derive such a column directly from the exact normalized Gamma pair by a bounded analytic linear mixer,

\[
\binom{S}{A}
=M(z)
\binom{1}{R_\infty(z)},
\qquad
M\in H^\infty(\mathbb H;M_2).
\tag{21}
\]

Because a Schur/Pythagorean column is bounded analytic, (15) forces the entire second column of `M` to vanish. Therefore `S` and `A` are independent of `R_infty`:

\[
\boxed{
\text{bounded analytic linear mixing of }(1,R_\infty)
\text{ cannot produce a nontrivial Pythagorean completion retaining the Gamma phase.}
}
\tag{22}
\]

This remains true even if `M` is not contractive, not unitary, not invertible, and not finite-state. The obstruction occurs **before** the positivity theorem is invoked: bounded analytic channelization has already erased the phase.

In particular, the tempting boundary-only Hadamard split

\[
S_0(t)=\frac{1+R_\infty(t)}2,
\qquad
A_0(t)=\frac{1-R_\infty(t)}2
\tag{23}
\]

satisfies on the real axis

\[
|S_0(t)|^2+|A_0(t)|^2=1,
\tag{24}
\]

because `|R_infty(t)|=1`. But neither pair can be the boundary trace of the corresponding bounded analytic column obtained by the same formulas in the upper half-plane: (4) rules out both nonconstant affine combinations. Thus a pointwise boundary Pythagorean identity is not enough to invoke the analytic positive-kernel machinery of `WP-182`.

## 4. Matched control: genuine inner phases do admit the same channel split

The obstruction is not a generic defect of two-channel completion.

Let `B` be any scalar inner function on the upper half-plane. Then

\[
S_B(z)=\frac{1+B(z)}2,
\qquad
A_B(z)=\frac{1-B(z)}2
\tag{25}
\]

belong to `H^infinity`, and their boundary values satisfy

\[
|S_B|^2+|A_B|^2=1
\tag{26}
\]

almost everywhere. Hence

\[
F_B=\binom{S_B}{A_B}
\tag{27}
\]

is a bounded analytic column with unit boundary norm; equivalently it is a standard lossless two-channel completion.

So exactly the same constant Hadamard mixing works for an ordinary inner phase. The difference is the analytic divisor: zeros of an inner function satisfy the Blaschke condition, whereas the Gamma phase zeros (2) do not.

This control rules out an interpretation in which (22) is merely an artifact of asking for two outputs or of the particular Pythagorean normalization. The failure is tied to the same infinite Gamma divisor that obstructs scalar and matrix passivity in `WP-170`--`WP-173`, now expressed as a stability obstruction for **all bounded analytic linear channel maps**.

## 5. Aggressive falsification and exact scope

Several possible escapes remain, and they are mathematically different from the route ruled out here.

**Boundary-only mixing is not excluded as an `L^infinity` identity.** Equation (23) already shows that one may split the unimodular boundary phase pointwise. What fails is the bounded analytic continuation required for ordinary Schur/de Branges--Rovnyak positivity. A boundary-only Hilbert-space construction would need its own domain and sign theorem.

**A singular or meromorphic mixer can cancel the divisor.** To remove the zeros (2) rather than inherit them, a coefficient must have poles or another singular mechanism at those points. Such a mixer is not in `H^infinity` and is outside the stable-channel theorem. This is a genuine remaining category, but it is precisely the kind of infinite singular compensation that `WP-170` already requires to be source-forced rather than inserted as a regularization.

**Nonlinear or linear-fractional transforms are not classified here.** A nonlinear function of `R_infty` need not inherit its zeros, and a quotient can cancel them. Such an operation would be new structure, not a bounded analytic linear channel completion. It must be justified intrinsically and then re-audited for poles, domains, positivity, and target fitting.

**The theorem acts after the relative phase has been formed.** `WP-169` derives `R_infty` as the quotient of two spectral factors with the same boundary modulus. A Mathia construction that couples the **unnormalized factors before quotienting** may alter the relevant analytic divisor and is not ruled out by (8)--(18). This is especially important for the line mandate: the surviving architecture should couple finite and archimedean information before scalarization, not isolate the known Gamma factor and then repair it.

**Smirnov/Nevanlinna, indefinite, or unbounded operator categories remain open.** The conclusion uses `H^infinity` boundedness. Moving to a larger class may be mathematically legitimate, but positivity is no longer inherited from ordinary bounded Schur channel theory and requires an independent coercivity theorem.

**No finite-prime or polar term has been produced.** The theorem is a negative boundary on the archimedean channel architecture. It does not identify the Mangoldt sector, the polar counterterms, or the global Weil quadratic form.

These boundaries prevent overclaiming. The exact conclusion is not that every two-channel or dissipative route fails; it is that a post-quotient **stable bounded analytic linear** repair of the exact Gamma phase cannot even reach the analytic class in which the `WP-182` positive completion lives.

## 6. Prior art and novelty audit

The function theory is classical. The only theorem needed for (8) is the standard Blaschke zero-set condition for nonzero Hardy/bounded analytic functions on a half-plane, already used and sourced in `WP-170`. Modern meromorphic-inner formulations state the same upper-half-plane condition

\[
\sum_n\frac{\operatorname{Im}z_n}{1+|z_n|^2}<\infty
\tag{28}
\]

for admissible inner zero sequences. No novelty is claimed for Blaschke factorization, `H^infinity` ideals, or the observation that multiplication by an analytic function cannot cancel zeros.

Likewise, `WP-182` already audits the classical Pythagorean-mate/de Branges--Rovnyak and Darlington completion theory. The matched inner split (25)--(27) is elementary standard Hardy-space algebra.

A targeted literature search found the expected standard Hardy/inner factorization and Pythagorean-mate literature, but no separate theorem is needed here beyond those classical ingredients. Absence of a paper with the present wording is not treated as evidence of novelty.

The Mathia-specific substantive delta is the combination of the **exact source-derived Gamma divisor** from `WP-169`--`WP-170` with the newly live Pythagorean escape of `WP-182`. It yields the dimension-independent channel theorem

\[
\boxed{
A+R_\infty B\in H^\infty,
\quad A,B\in H^\infty
\Longrightarrow
B=0,
}
\tag{29}
\]

and therefore closes an explicit bridge that was not settled by merely observing that `R_infty` itself is non-Schur.

This is a project-specific no-go obtained from classical factorization, not a new theorem of Hardy-space theory and not a claim of Weil positivity.

## 7. Consequence for the Weil-positivity search

`WP-182` remains an important structural escape from the scalar dissipative finite-part obstruction: a signed scalar phase can participate in a larger positive completed channel. `WP-183` shows, however, that the exact phase exposed by `WP-169` cannot be attached to that architecture **after quotienting** by any bounded analytic linear filter bank. The non-Blaschke Gamma divisor survives every nonzero bounded multiplier.

The surviving source-to-destination gate is therefore sharper:

\[
\boxed{
\text{do not isolate }R_\infty\text{ first and then try to stabilize it linearly;}\
\text{the coupling must occur before the quotient or change analytic category genuinely.}
}
\tag{30}
\]

For the branch mandate, the most relevant remaining test is now upstream. One must inspect whether the Mathia-native finite/archimedean source can produce a coupled pair or operator **before** the Nyman/Gamma relative phase is divided out, in such a way that the troublesome infinite divisor is absorbed by the same geometry that also retains the signed finite-prime information. If instead the construction first identifies the known Gamma phase and only afterward introduces a bounded Schur/Pythagorean channel completion, (29) shows that the phase has necessarily been erased.

This does not solve the global Weil sign problem. It removes a broad stable-linear postprocessing class and further concentrates the search on genuinely pre-scalar, source-derived finite--archimedean coupling, singular/domain-changing geometry with an independent sign theorem, or another mechanism that does more than repackage the known functional-equation phase.

## Dependencies

- `research/weil_positivity/findings/WP-169-pointed-nyman-relative-phase-is-exact-archimedean-scattering.md`
- `research/weil_positivity/findings/WP-170-archimedean-phase-is-not-a-passive-inner-boundary-response.md`
- `research/weil_positivity/findings/WP-171-matrix-inner-passivity-forces-positive-boundary-delay.md`
- `research/weil_positivity/findings/WP-173-passive-hilbert-termination-of-regular-j-contractive-channels-collapses-back-to-schur.md`
- `research/weil_positivity/findings/WP-182-pythagorean-defect-completion-cancels-dissipative-pole-but-controls-total-phase.md`
