# WP-190 — Prime Circle's positive Poisson ray is Burnol's p-adic time delay, while the Weil block is its conductor defect

**Status:** `LITERATURE+DERIVED + EXACT-IDENTIFICATION + INDEPENDENT-POSITIVITY-CARRIER + PRIOR-ART-CLASSICALIZATION + DECISIVE-REDIRECT + NOT-WEIL-POSITIVITY`.

`WP-001` isolates the Prime-Circle prime-ray Poisson matrix

\[
K_p(a,b)=(\log p)p^{-|a-b|/2},\qquad a,b\ge 1,
\tag{1}
\]

as an independently positive completion of the exact finite-place off-diagonal Weil coefficients, and shows that the actual zero-diagonal finite-prime Weil block is

\[
A_p=(\log p)I-K_p.
\tag{2}
\]

A targeted audit of Burnol's p-adic scattering theory sharpens the prior-art boundary substantially. For the unramified trivial-character sector of \(\mathbb Q_p\), Burnol's **nonnegative scattering time-delay operator** has exactly the Poisson symbol whose Hardy/Fourier Toeplitz compression is (1). Moreover Burnol's conductor operator on that same sector is exactly the affine defect (2).

Thus the two Mathia objects are not merely analogous to a classical local scattering construction:

\[
\boxed{
K_p=\operatorname{Toep}(T_p),
\qquad
A_p=\operatorname{Toep}(H_p),
\qquad
H_p=(\log p)-T_p.
}
\tag{3}
\]

Here `Toep` denotes compression of the circle multiplier to the nonnegative Fourier modes corresponding to the exponent ray. Burnol proves \(T_p\ge0\) by an independent scattering theorem, while the local explicit-formula observable is organized through the conductor operator and an odd/even supertrace. The positive operator is therefore **the completed carrier**, not the signed Weil block.

This is a decisive classicalization of the local Prime-Circle positivity route. It also gives the finite-place analogue of `WP-189`: an exact local explicit-formula carrier may coexist with a strong independent positivity theorem without that positivity ordering the actual Weil observable.

## 1. Burnol's trivial unramified time delay is the Poisson kernel

Burnol works over a nonarchimedean local field with residue-field size \(q\), different exponent \(\delta\), and multiplicative spectral coordinate \(z\in\mathbb T\). His scattering matrix is diagonal in the unit characters. In the trivial-character sector the time-delay spectral function is

\[
T(1;z)
=
(\log q)
\left(
\delta+
\frac{1-q^{-1}}{|1-z/\sqrt q|^2}
\right).
\tag{4}
\]

Specialize to \(\mathbb Q_p\). Then

\[
q=p,
\qquad
\delta=0.
\tag{5}
\]

Writing

\[
L=\log p,
\qquad
r=p^{-1/2},
\qquad
z=e^{i\theta},
\tag{6}
\]

gives

\[
\boxed{
T_p(\theta)
=
L\frac{1-r^2}{|1-r e^{i\theta}|^2}
=L P_r(\theta),
}
\tag{7}
\]

where \(P_r\) is the ordinary circle Poisson kernel. Its Fourier series is

\[
P_r(\theta)
=
\sum_{n\in\mathbb Z}r^{|n|}e^{in\theta}.
\tag{8}
\]

Let \(e_a(\theta)=e^{ia\theta}\), \(a\ge1\), and compress multiplication by \(T_p\) to the positive Fourier ray. Equations (7)--(8) give exactly

\[
\begin{aligned}
\langle e_a,T_p e_b\rangle
&=L r^{|a-b|}\\
&=(\log p)p^{-|a-b|/2}\\
&=K_p(a,b).
\end{aligned}
\tag{9}
\]

Thus the positive Poisson/GCD-type completion isolated in `WP-001` is the Hardy Toeplitz compression of Burnol's classical p-adic time-delay multiplier.

No arithmetic interpolation, zero data, or RH assumption enters this identification. It is an exact equality after the natural specialization \(q=p\), \(\delta=0\).

## 2. The positivity theorem is genuinely independent

Burnol's time-delay operator is not declared positive from its final scalar formula alone. It is obtained from the interaction projector in the scattering system. For the interacting projection \(K\) and multiplicative dilation representation \(U(t)\), Burnol derives the quadratic-form identity

\[
\langle Tf,f\rangle
=
\int_{\mathbb Q_p^\times}
\|K U(t)f\|^2\,d^\times t
\ge0.
\tag{10}
\]

The time delay is therefore a nonnegative self-adjoint scattering observable for a structural reason. Equation (7) is consistent with this theorem because the Poisson kernel is pointwise positive.

This is exactly the sort of local theorem that can look tempting for the `weil_positivity` mandate: the correct prime scale appears intrinsically and the sign is independent of RH. The next calculation shows why it still does not supply Weil positivity.

## 3. Burnol's conductor defect is exactly the zero-diagonal Weil block

Burnol relates the time-delay operator \(T\) and the local conductor operator \(H\). On the trivial unit-invariant component his spectral decomposition gives

\[
T-\delta\log q
=
-H+(\delta+1)\log q.
\tag{11}
\]

For \(\mathbb Q_p\), equation (5) reduces this to

\[
\boxed{
H_p=L-T_p.
}
\tag{12}
\]

Compressing (12) to the same positive Fourier ray and using (9),

\[
\begin{aligned}
\langle e_a,H_p e_b\rangle
&=L\delta_{ab}-Lr^{|a-b|}\\
&=(\log p)\delta_{ab}
-(\log p)p^{-|a-b|/2}\\
&=A_p(a,b).
\end{aligned}
\tag{13}
\]

Therefore the matrix called \(A_p\) in `WP-001` is exactly the Toeplitz compression of Burnol's trivial-character conductor multiplier. In particular,

\[
A_p(a,a)=0,
\qquad
A_p(a,b)=-(\log p)p^{-|a-b|/2}\quad(a\ne b),
\tag{14}
\]

so the adjacent two-mode restriction has eigenvalues

\[
\pm(\log p)p^{-1/2}.
\tag{15}
\]

The loss of positivity is therefore not an artifact of Mathia's matrix packaging. It is already the classical relation between p-adic scattering time delay and the conductor observable:

\[
\boxed{
\text{positive time delay }T_p
\quad\xrightarrow{\;L-\,\cdot\;}\quad
\text{indefinite conductor/Weil block }H_p.
}
\tag{16}
\]

The scalar diagonal \(L\) is precisely the positive completion term that `WP-001` showed cannot simply be retained in the finite-place Weil functional.

## 4. The local explicit formula uses the conductor through a supertrace

Burnol's local trace formula makes the distinction sharper. He grades the interacting scattering space into an odd one-dimensional Tate direction and its even orthogonal complement, and proves a supertrace identity of the form

\[
\operatorname{sTr} Z(f)+f(1)\log q
=H(f)(1),
\tag{17}
\]

where \(H(f)(1)\) is the local contribution to Weil's explicit formula in his normalization.

Thus the same classical construction contains both structures:

\[
T_p\ge0
\quad\text{from interaction probability},
\tag{18}
\]

while the explicit-formula information is carried by

\[
H_p=L-T_p
\quad\text{and by the graded supertrace organization}. 
\tag{19}
\]

Ordinary positivity and the local Weil observable are therefore separated before any global Riemann problem is considered. The sign-sensitive arithmetic term is obtained only after an affine subtraction / grading operation that does not preserve ordinary positive-semidefinite order.

This is stronger than the qualitative prior-art warning already recorded in `WP-001`: the Prime-Circle matrix itself can now be identified coefficient-for-coefficient with the classical time-delay operator, and its Weil defect with the classical conductor multiplier.

## 5. Adversarial controls

### The Hardy compression does not create the match

The full multiplier \(T_p\) has the bilateral Toeplitz matrix

\[
Lr^{|a-b|},\qquad a,b\in\mathbb Z.
\]

Restricting to \(a,b\ge1\) merely selects the exponent-ray principal compression. No coefficient is fitted in the compression. Positivity also survives compression because it comes from multiplication by the positive function \(T_p(\theta)\).

### The normalization is forced

For \(\mathbb Q_p\), the local invariants are exactly \(q=p\) and \(\delta=0\). The spectral radius in (7) is therefore \(r=p^{-1/2}\), not a tunable damping parameter. The Fourier coefficient at separation \(k\) is exactly

\[
(\log p)p^{-k/2},
\tag{20}
\]

which is the critical finite-place scale in `WP-001`.

### The diagonal check fixes the affine constant

Since \(\widehat P_r(0)=1\), the diagonal of \(T_p\) is exactly \(L\). Hence \(L-T_p\) has exactly zero diagonal. Any different affine subtraction would fail the `WP-001` coefficient/diagonal audit.

### Ramified characters do not rescue the Riemann sector

Burnol's ramified character sectors carry conductor-exponent terms and different affine branches. They are genuine parts of the local scattering theory but are not the unramified trivial component that produces the Riemann prime-power ray. Importing a ramified sector to repair the sign would change the target local object rather than explain the sign of (13).

### Positivity contains no zero information

The theorem \(T_p\ge0\) exists for the local field independently of the global zeta zero divisor. It therefore passes the branch's removal-of-zero-data control, but precisely for that reason it is also a matched control: local positive scattering is too universal to force global Riemann positivity by itself.

### There is still no finite--archimedean sign theorem

Nothing in the local identity (3) produces the Gamma contribution or the polar/global counterterms. Adding those terms by hand would violate the mandate. `WP-189` supplies a complementary archimedean warning: Burnol's exact Gamma reflection can itself be carried by nonnegative supersymmetric Hamiltonians while the relevant phase velocity still changes sign. The finite and real places therefore exhibit the same structural lesson in different operator categories: **positivity of a local carrier is not positivity of the explicit-formula observable**.

## 6. Prior art and novelty assessment

No novelty is claimed for p-adic scattering, the time-delay theorem, the conductor operator, the Poisson kernel, or Burnol's local supertrace formula.

The primary source is:

- Jean-François Burnol, *Scattering on the p-adic field and a trace formula*, International Mathematics Research Notices 2000, no. 2, 57--70, DOI `10.1155/S1073792800000040`, arXiv `math/9901051`. Burnol constructs the local scattering matrix, proves nonnegativity of time delay, derives the explicit trivial-character spectral function, relates time delay to the conductor operator, and recovers the local explicit-formula contribution through a graded supertrace.

`research/weil_positivity/SOURCES.md` already records this source as the main prior-art warning for `WP-001`; no new source category is needed here.

The Mathia-specific durable delta is the exact identification (3). `WP-001` had already noted that Burnol's local time delay is positive while the Weil term is supertracial, but it did not identify the Prime-Circle Poisson matrix with that time delay or identify its zero-diagonal defect matrix with the conductor multiplier. Equations (9) and (13) close that gap.

This is therefore a **prior-art classicalization and redirection**, not a claim that Mathia has rediscovered a new p-adic scattering theorem.

## 7. Consequence for `weil_positivity`

The local Prime-Circle Poisson completion no longer qualifies even as a potentially novel positive finite-place mechanism. In the exact Riemann normalization it is a classical p-adic scattering time-delay operator. More importantly, the same classical theory already exhibits the precise failure mode that the branch must avoid:

\[
\boxed{
\text{independently positive local carrier}
\not\Rightarrow
\text{positive local Weil observable}.
}
\tag{21}
\]

The signed Weil block is the conductor defect of that carrier, and the local explicit formula uses an affine/grading operation rather than ordinary positivity.

Combined with `WP-189`, this sharply localizes where a surviving mechanism can still be new. It cannot consist merely of placing independently positive scattering systems at the finite primes and at infinity and then reading off their phases or time delays. The required sign theorem must act on a **single assembled finite--archimedean observable** after whatever source-forced coupling, quotient, relative index, renormalization, or noncommutative operation creates the exact Weil decomposition.

A successful continuation must therefore exhibit all of the following before it can count as the sought mechanism:

1. a source-forced coupling that is not the direct sum of the classical local carriers;
2. the finite conductor defects, Gamma term, and polar/global counterterms as outputs of the same completed object;
3. an independent geometric theorem ordering that assembled observable itself;
4. survival of the sign after the final quotient/compression/regularization, without inserting the Weil functional or zero divisor by definition.

The present finding closes only the local Poisson/time-delay route. It does not rule out a genuinely global cohomological, noncommutative, singular-relative, or nonseparable finite--archimedean construction.

## Dependencies

- `research/weil_positivity/findings/WP-001-prime-local-positive-rays-cannot-be-weil-summands.md`
- `research/weil_positivity/findings/WP-189-burnol-gamma-reflection-has-positive-supersymmetric-hamiltonians-but-no-weil-sign.md`
- `research/weil_positivity/SOURCES.md`

## Bottom line

For \(\mathbb Q_p\), Burnol's independently nonnegative scattering time delay is exactly the Poisson multiplier

\[
T_p=(\log p)P_{p^{-1/2}},
\]

whose exponent-ray Toeplitz compression is the positive Prime-Circle matrix \(K_p\). Burnol's conductor operator on the same unramified trivial sector is exactly

\[
H_p=(\log p)-T_p,
\]

whose Toeplitz compression is the zero-diagonal indefinite Weil matrix \(A_p\).

The local sign problem is therefore already present in the classical p-adic scattering model in exactly the Mathia normalization. The positive geometry belongs to the carrier; the explicit-formula observable appears only after an order-destroying affine/grading step. Any genuinely new Weil-positive mechanism must live in the global assembly, not in this local Poisson positivity.