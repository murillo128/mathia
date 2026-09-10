# MC-194 — The full additive primorial spectrum has a multiplicity-free arithmetic image

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-190` rules out principal/nonprincipal coupling by unit-group-equivariant linear or Hermitian-quadratic statistics on one residue-class vector. `MC-191` shows that the canonical nested-primorial bonding maps remain character-sector diagonal. `MC-192` and `MC-193` then move to additive Fourier coordinates and show, shell by shell, that primitive rational additive phases are Gauss-weighted re-encodings of coarse multiplicative character sectors.

There is one remaining ambiguity in that shell-local picture: the **ambient full additive frequency space contains several copies of the same multiplicative character at different denominator shells**, so an operator coupling different shells might appear able to create information absent from each shell separately.

For the actual additive transform of a single unit-supported residue vector, that multiplicity is illusory. The full additive profile lies in a special invariant subspace isomorphic to the regular representation of the unit group, hence **each multiplicative character occurs exactly once in the arithmetic image**. All shell copies of a fixed character are rigid scalar multiples of the same source Fourier coefficient.

Let `q` be square-free,

\[
G_q=(\mathbb Z/q\mathbb Z)^\times,
\]

and let `A:G_q\to\mathbb C`. Define the zero-extended additive Fourier profile

\[
(\mathcal K_qA)(h)
:=
\sum_{a\in G_q}A(a)e\!\left(\frac{ha}{q}\right),
\qquad h\in\mathbb Z/q\mathbb Z.
\tag{1}
\]

For `b\in G_q`, let

\[
(\tau_bA)(a)=A(b^{-1}a),
\qquad
(\sigma_bF)(h)=F(bh).
\tag{2}
\]

Then

\[
\boxed{\mathcal K_q\tau_b=\sigma_b\mathcal K_q.}
\tag{3}
\]

Moreover `\mathcal K_q` is injective: it is the ordinary discrete Fourier transform of the zero extension of `A` from the units to all of `\mathbb Z/q\mathbb Z`, and the full discrete Fourier transform is invertible. Therefore

\[
\mathcal I_q:=\operatorname{im}\mathcal K_q
\tag{4}
\]

is a `G_q`-invariant subspace equivariantly isomorphic to the regular representation `L^2(G_q)`. Since `G_q` is finite abelian,

\[
\boxed{
\mathcal I_q=\bigoplus_{\chi\in\widehat G_q}\mathcal I_q(\chi),
\qquad
\dim \mathcal I_q(\chi)=1.
}
\tag{5}
\]

Thus the arithmetic image is multiplicity-free even though the ambient additive frequency space is not.

The shell coordinates make this rigidity explicit. For each divisor `r|q`, let

\[
H_r=
\left\{\frac qr c\pmod q:c\in G_r\right\},
\qquad G_r=(\mathbb Z/r\mathbb Z)^\times,
\tag{6}
\]

with `H_1={0}`. The nonzero shells are exactly those of `MC-192`--`MC-193`; multiplication by `G_q` preserves every `H_r`, and its action on that shell factors through the regular action of `G_r`.

Fix a character `\chi\in\widehat G_q` with conductor `f_\chi`. A copy of `\chi` occurs in the ambient shell `H_r` exactly when

\[
f_\chi\mid r\mid q.
\tag{7}
\]

Let `\chi_r` be the character modulo `r` inducing `\chi` by inflation. If `E_r` denotes the shell function

\[
E_r(c):=(\mathcal K_qA)((q/r)c),
\qquad c\in G_r,
\tag{8}
\]

then the Gauss-transform identity of `MC-193`, applied to the pushforward from `G_q` to `G_r`, gives

\[
\boxed{
\widehat E_r(\overline{\chi_r})
=
\tau_r(\chi_r)
\frac{\varphi(q)}{\varphi(r)}
\widehat A_q(\chi),
\qquad f_\chi\mid r\mid q.
}
\tag{9}
\]

For square-free `r`, the induced-character Gauss sum is nonzero and

\[
|\tau_r(\chi_r)|=\sqrt{f_\chi}.
\tag{10}
\]

Consequently all ambient shell copies of `\chi` that are actually reached by `(1)` lie on the single line

\[
\boxed{
\left(
\tau_r(\chi_r)\frac{\varphi(q)}{\varphi(r)}
\right)_{f_\chi\mid r\mid q}
\widehat A_q(\chi).
}
\tag{11}
\]

There are no independent cross-shell `\chi` degrees of freedom in the image.

It follows that **every `G_q`-invariant Hermitian quadratic form on the actual full additive profile**, including forms with arbitrary cross-denominator couplings in the ambient frequency coordinates, restricts to

\[
\boxed{
Q(\mathcal K_qA)
=
\sum_{\chi\in\widehat G_q}
m(\chi)|\widehat A_q(\chi)|^2,
\qquad m(\chi)\in\mathbb R.
}
\tag{12}
\]

If `Q` is positive semidefinite on `\mathcal I_q`, then `m(\chi)\ge0` for all `\chi`. Cross-shell interference can change the single scalar weight `m(\chi)` assigned to a character, but it cannot create a principal/nonprincipal cross term.

For the rough Möbius residue vector

\[
A_q(X;a)=
\sum_{\substack{n\le X\\n\equiv a\pmod q}}\mu(n),
\tag{13}
\]

the principal coefficient is

\[
\widehat A_q(1)=\frac{G_q(X)}{\varphi(q)},
\qquad
G_q(X)=\sum_{\substack{n\le X\\(n,q)=1}}\mu(n).
\tag{14}
\]

Equation `(9)` becomes, on every shell,

\[
\boxed{
\widehat E_r(1)
=
\mu(r)\frac{G_q(X)}{\varphi(r)}.
}
\tag{15}
\]

Hence even an arbitrary unit-equivariant quadratic coupling among **all** rational denominator shells has the same dichotomy as `MC-190`: if its principal weight `m(1)` vanishes, it is blind to `G_q`; if `m(1)>0` in a positive form, it controls `G_q` only because `|G_q|^2` is directly present in `(12)`. It cannot infer the rough zero mode from transverse character cancellation.

This closes the unit-equivariant cross-denominator loophole left after `MC-193`. A viable additive-spectrum continuation must now break the common unit action in a source-forced way, use genuinely nonlinear arithmetic structure whose representation products can land in the principal sector, or pay for the principal rough mode independently.

## 1. The full additive transform intertwines the unit action

Starting from `(1)` and `(2)`, change variables `a=bu`:

\[
\begin{aligned}
(\mathcal K_q\tau_bA)(h)
&=\sum_{a\in G_q}A(b^{-1}a)e(ha/q)\\
&=\sum_{u\in G_q}A(u)e(hbu/q)\\
&=(\mathcal K_qA)(bh)\\
&=(\sigma_b\mathcal K_qA)(h).
\end{aligned}
\tag{16}
\]

This proves `(3)`. No analytic-number-theory estimate is used.

Now extend `A` by zero to a function `\widetilde A` on the finite additive group `\mathbb Z/q\mathbb Z`. Equation `(1)` is exactly the finite additive Fourier transform of `\widetilde A`. Fourier inversion on `\mathbb Z/q\mathbb Z` reconstructs `\widetilde A`, so `\mathcal K_q` is injective.

The source representation is the regular multiplicative representation of the finite abelian group `G_q`. Its characters form an orthogonal basis and each character occurs with multiplicity one. Intertwining plus injectivity therefore proves `(5)`.

The important distinction is between the ambient codomain and the arithmetic image. The permutation representation of `G_q` on all additive frequencies generally has repeated character sectors, because different gcd/denominator shells carry quotient regular representations. But the image of one unit-supported source vector family occupies only one coherent copy of every source character across those repeated ambient sectors.

## 2. Denominator shells describe the ambient multiplicities

Multiplication by a unit does not change `gcd(h,q)`, so the orbits of `G_q` on `\mathbb Z/q\mathbb Z` are exactly the sets `(6)`, indexed by `r|q`. On `H_r`, writing `h=(q/r)c` identifies the action with multiplication of `c` by the reduction of `G_q` to `G_r`. Because the reduction map is surjective for `r|q`, the shell representation is the regular representation of `G_r`, inflated to `G_q`.

A character of `G_q` occurs in that inflated representation exactly when it factors through `G_r`. For square-free `q`, this is equivalent to its conductor dividing `r`, proving `(7)`.

Thus a character of small conductor can occur in many ambient shells. The principal character occurs in every shell. This is the apparent extra multiplicity that a cross-denominator kernel could try to exploit.

But `MC-193` already computes the shell transform exactly. The pushforward of `A` from `G_q` to `G_r` has normalized `\chi_r` coefficient

\[
\widehat B_r(\chi_r)
=
\frac{\varphi(q)}{\varphi(r)}\widehat A_q(\chi),
\tag{17}
\]

and the primitive additive transform multiplies it by `\tau_r(\chi_r)` and conjugates the character label. This gives `(9)`. Since `(10)` makes every multiplier nonzero, the vector `(11)` is a genuine one-dimensional diagonal embedding through all eligible shell copies.

For the principal character, `\tau_r(1)=\mu(r)` on square-free `r`, giving `(15)` and recovering the Ramanujan-shell relation of `MC-192` after multiplying by `\varphi(r)`.

## 3. Arbitrary equivariant cross-shell quadratic forms still diagonalize on the image

Let `B` be the sesquilinear form associated with a `G_q`-invariant Hermitian quadratic form on `\mathcal I_q`. Take vectors `v_\chi\in\mathcal I_q(\chi)` and `v_\psi\in\mathcal I_q(\psi)`. Under the unit action they transform by their respective one-dimensional characters, up to the harmless conjugation convention fixed by `(2)`.

Invariance gives

\[
B(v_\chi,v_\psi)
=
\chi(b)\overline{\psi(b)}B(v_\chi,v_\psi)
\qquad(b\in G_q).
\tag{18}
\]

If `\chi\ne\psi`, choose `b` with `\chi(b)\ne\psi(b)`; then `(18)` forces

\[
B(v_\chi,v_\psi)=0.
\tag{19}
\]

Since every isotypic component of `\mathcal I_q` is one-dimensional, the restriction of `B` to each component is multiplication by one real number `m(\chi)`. This proves `(12)`.

An ambient invariant operator is allowed to mix the several copies of the **same** character that live in different shells. Such mixing can be represented by an arbitrary Hermitian matrix on that ambient multiplicity space. Equation `(11)` shows what happens after restriction to the arithmetic image: the whole matrix is evaluated on one fixed shell-amplitude vector and collapses to the single scalar `m(\chi)`. It never produces a term involving a different character.

In particular, all cross-shell principal coordinates are proportional to the same number `G_q(X)`. Their interference can amplify, attenuate, or annihilate the direct principal contribution, but it cannot convert nonprincipal estimates into information about `G_q`.

## 4. Consequence for the active logarithmic primorial

Take

\[
q=q_y=\prod_{p\le y}p,
\qquad y=c\log X,
\tag{20}
\]

as in `MC-180`--`MC-193`. `MC-188` provides strong signed dispersion in nonprincipal residue/character directions but leaves `G_{q_y}(X)` without a fixed-power bound. `MC-189` shows that the proved function-field analogue pays its principal mode separately. `MC-190`--`MC-191` eliminate same-modulus and canonical nested-modulus equivariant coupling, while `MC-192`--`MC-193` eliminate a shell-local additive-basis shortcut.

The present result shows that allowing a quadratic kernel to see **all rational additive shells simultaneously** still does not help as long as the kernel respects the common multiplicative action of `G_{q_y}`. The ambient shell multiplicities do not correspond to independent arithmetic observations; they are repeated encodings of the same one-dimensional source character coefficient.

Accordingly, the additive-spectrum escape class narrows to mechanisms that violate at least one hypothesis of `(12)` for an arithmetic reason. Examples not ruled out are:

- an archimedean or interval-boundary weight on additive frequencies whose failure of unit-equivariance is quantitatively tied to the ordering `n\le X`;
- a nonlinear cross-character identity in which a product such as `\chi_1\chi_2\cdots\chi_k=1` can enter the principal sector and whose coefficients are controlled independently;
- a cross-scale statistic carrying source data not recoverable from one residue vector and its Fourier image;
- an independent fixed-power estimate for the principal rough sum itself.

These are escape categories, not evidence that any one succeeds.

## 5. Prior art and novelty audit

The underlying representation theory is standard. Fourier analysis on a finite abelian group diagonalizes its regular representation into one-dimensional characters with multiplicity one; this is the same classical machinery already audited in `MC-190` against Audrey Terras, *Fourier Analysis on Finite Groups and Applications*, Cambridge University Press (1999), Part I. The additive Fourier transform and the unit-action intertwining calculation `(16)` are elementary finite harmonic analysis.

The shell multiplier `(9)` is the Gauss-sum identity established in `MC-193` from standard Dirichlet-character theory; Montgomery and Vaughan, *Multiplicative Number Theory I: Classical Theory*, Chapter 9, supply the induced-character Gauss-sum formula used there. No novelty is claimed for regular-representation multiplicities, Fourier inversion, conductor factorization through quotient unit groups, Gauss sums, or character orthogonality.

A targeted prior-art search over finite-abelian Fourier analysis, regular representations, induced characters, and Gauss transforms found the standard component theorems but no reason to claim the combined statement as a new theorem of harmonic analysis or analytic number theory. The durable Mathia delta is the **frontier classification**: once the full rational additive spectrum is restricted to profiles actually arising from one primorial residue vector, its apparent cross-shell representation multiplicity collapses to a multiplicity-free arithmetic image. Therefore the cross-denominator unit-equivariant quadratic escape left open after `MC-193` is not a new source of principal/transverse coupling.

## 6. Boundaries and falsification checks

- The square-free hypothesis is used for the clean nonvanishing and magnitude `(10)` on every divisor shell. The multiplicity-free image statement `(5)` itself follows from injectivity and the regular source representation and does not require square-freeness, but the explicit all-shell vector `(11)` is stated only in the primorial regime where the Gauss multipliers are nonzero.
- The theorem concerns the image of a **single** unit-supported residue vector under its complete additive Fourier transform. If a construction supplies genuinely independent data at several scales, cutoffs, or moduli rather than deterministic transforms of one vector, its joint representation can have real multiplicity and lies outside this result.
- `G_q`-invariance is decisive. A source-forced non-equivariant weight can mix character sectors. Such a proposal must quantify the symmetry-breaking term and show that it carries fixed-power information rather than merely inserting the interval endpoint by hand.
- Hermitian quadratic forms are classified only after restriction to `\mathcal I_q`. An ambient form may have arbitrary matrices between repeated shell copies of the same character; `(11)` shows why those matrices collapse to one scalar on actual arithmetic profiles.
- A nonlinear invariant can couple characters whose product is principal. Nothing here proves that such a coupling has a useful sign, size, or independently available bound.
- If `m(1)>0`, a positive quadratic estimate can legitimately bound `G_q`; the obstruction is only to claiming that transverse cancellation forced the principal bound. The proof must still obtain the total energy estimate without assuming an equivalent Mertens input.

The finding would be falsified by a `G_q`-invariant Hermitian quadratic form on the actual full additive profiles whose restriction contains a nonzero term `\widehat A_q(1)\overline{\widehat A_q(\chi)}` for some `\chi\ne1`. Equations `(3)`--`(5)` and `(18)`--`(19)` exclude exactly that possibility.

## Consequence

The rational additive spectrum no longer supplies an unexplored equivariant loophole merely because the same finite-group character appears in several denominator shells. Those repeated ambient copies are locked together by the exact Fourier/Gauss image of the original residue vector.

The next useful continuation should therefore stop searching for a clever **unit-equivariant cross-shell quadratic kernel**. To cross the fixed-power rough-zero-mode boundary, the new information must come from source-forced symmetry breaking, nonlinear arithmetic coupling, genuinely independent multiscale data, or direct principal-mode control.