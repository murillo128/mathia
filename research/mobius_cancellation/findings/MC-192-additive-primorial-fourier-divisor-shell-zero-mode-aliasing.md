# MC-192 — Additive primorial Fourier divisor shells alias the rough zero mode

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-188` isolates the logarithmically rough Möbius sum as the principal character coefficient left uncontrolled by smooth-modulus dispersion. `MC-190` and `MC-191` then show that multiplicative-unit-group equivariant quadratic statistics and canonical nested-primorial transport cannot mix that principal coefficient with transverse Dirichlet-character sectors.

A natural way to break that diagonalization is to stop using multiplicative characters and instead take the **additive Fourier transform of the same primorial residue vector**. This really is a different, non-multiplicatively-equivariant representation, but it does not make the rough zero mode cheaper. On every divisor-denominator shell, the additive modes contain an exact Ramanujan-sum copy of the rough principal coefficient; on the denominator-two shell the copy is literally a single nonzero additive frequency.

Let `q` be square-free and define

\[
A_q(X;a)
:=
\sum_{\substack{n\le X\\n\equiv a\pmod q}}\mu(n),
\qquad a\in (\mathbb Z/q\mathbb Z)^\times,
\tag{1}
\]

with rough zero mode

\[
G_q(X)
:=
\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}A_q(X;a)
=
\sum_{\substack{n\le X\\(n,q)=1}}\mu(n).
\tag{2}
\]

Zero-extend `A_q` to all residue classes modulo `q` and take its additive transform

\[
\mathcal A_q(h;X)
:=
\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
A_q(X;a)e\!\left(\frac{ha}{q}\right)
=
\sum_{\substack{n\le X\\(n,q)=1}}
\mu(n)e\!\left(\frac{hn}{q}\right),
\tag{3}
\]

where `e(t)=exp(2 pi i t)`.

For every divisor `r|q`, `r>1`, define the reduced-denominator shell

\[
H_r
:=
\left\{\frac qr a\pmod q:
 a\in(\mathbb Z/r\mathbb Z)^\times\right\}.
\tag{4}
\]

Then

\[
\boxed{
\sum_{h\in H_r}\mathcal A_q(h;X)
=
\mu(r)G_q(X).
}
\tag{5}
\]

Equivalently, writing the shell directly at denominator `r`,

\[
E_{q,r}(a;X)
:=
\sum_{\substack{n\le X\\(n,q)=1}}
\mu(n)e\!\left(\frac{an}{r}\right),
\qquad (a,r)=1,
\tag{6}
\]

one has

\[
\boxed{
G_q(X)
=
\mu(r)\sum_{a\bmod r}^{*}E_{q,r}(a;X).
}
\tag{7}
\]

For the active logarithmic primorial

\[
q_y=\prod_{p\le y}p,
\tag{8}
\]

`q_y` is square-free and, once `y>=2`, even. Taking `r=2` in `(5)` gives the sharpest form of the obstruction:

\[
\boxed{
\mathcal A_{q_y}(q_y/2;X)=-G_{q_y}(X).
}
\tag{9}
\]

Indeed every integer coprime to `q_y` is odd, so `e(n/2)=-1` term by term. Thus a **nonzero additive frequency of the primorial residue vector is exactly the hard rough Möbius zero mode with a minus sign**.

This kills the simplest additive-Fourier escape from `MC-190`--`MC-191`: nonzero additive frequency cannot be identified with transverse arithmetic information. The multiplicative principal sector is spread differently in additive coordinates, and the denominator-two mode is an exact alias rather than an independently controllable oscillatory direction.

More generally `(7)` gives the rate ledger

\[
\boxed{
\max_{a\bmod r}^{*}|E_{q,r}(a;X)|
\ge
\frac{|G_q(X)|}{\varphi(r)}.
}
\tag{10}
\]

Hence a bound

\[
\max_{a\bmod r}^{*}|E_{q,r}(a;X)|
\le X^{1-\delta+o(1)},
\qquad
\varphi(r)=X^{\alpha+o(1)},
\tag{11}
\]

can yield at best

\[
|G_q(X)|
\le X^{1-\delta+\alpha+o(1)}.
\tag{12}
\]

For a fixed or subpower divisor `r=X^{o(1)}`, any fixed-power additive-twist gain transfers to `G_q` with only subpower loss and is therefore already a fixed-power rough-Mertens theorem. At a polynomial-size denominator, individual-mode cancellation may genuinely be easier, but the `\varphi(r)` reconstruction multiplicity spends the corresponding polynomial exponent unless an additional source-side cancellation across the shell is proved.

So the additive basis does expose a real representation change, but **basis change alone does not couple the rough zero mode to the already-controlled transverse dispersion. It relocates the hard mode into low-denominator additive aliases and, at larger denominators, trades modewise cancellation against reconstruction cardinality.**

## 1. Ramanujan orthogonality proves the divisor-shell identity

Fix `r|q`. Because `q` is square-free, so is `r`. Every integer contributing to `(2)` satisfies `(n,q)=1`, hence also `(n,r)=1`.

Summing `(6)` over primitive residues `a (mod r)` gives

\[
\begin{aligned}
\sum_{a\bmod r}^{*}E_{q,r}(a;X)
&=
\sum_{\substack{n\le X\\(n,q)=1}}
\mu(n)
\sum_{a\bmod r}^{*}
e\!\left(\frac{an}{r}\right)\\
&=
\sum_{\substack{n\le X\\(n,q)=1}}
\mu(n)c_r(n),
\end{aligned}
\tag{13}
\]

where `c_r(n)` is the classical Ramanujan sum. For square-free `r` and `(n,r)=1`, the standard formula

\[
c_r(n)=\mu(r)
\tag{14}
\]

is constant. Therefore

\[
\sum_{a\bmod r}^{*}E_{q,r}(a;X)
=
\mu(r)G_q(X).
\tag{15}
\]

Since `mu(r)^2=1`, this is exactly `(7)`.

Now every `h in H_r` has the form `h=(q/r)a` with `(a,r)=1`, and

\[
e\!\left(\frac{hn}{q}\right)
=
e\!\left(\frac{an}{r}\right).
\tag{16}
\]

Thus `(15)` is equivalent to the `q`-Fourier shell identity `(5)`.

Nothing analytic has entered: `(5)` is finite additive-character orthogonality plus the classical Ramanujan-sum value on units. It is valid for every real `X>=1`.

## 2. The parity shell is an exact nonzero-frequency copy

For the logarithmic primorial `q_y`, take `r=2`. The shell `(4)` contains only

\[
H_2=\{q_y/2\}.
\tag{17}
\]

Every `n` with `(n,q_y)=1` is odd, so

\[
e\!\left(\frac{(q_y/2)n}{q_y}\right)
=e(n/2)
=-1.
\tag{18}
\]

Substituting in `(3)` proves `(9)` directly.

This is stronger than saying that the additive basis has some overlap with the multiplicative principal character. The relevant nonzero Fourier coefficient is **identical term by term** to the principal rough sum. Therefore any estimate advertised as uniform over all nonzero additive frequencies necessarily includes the original zero-mode problem unchanged.

The phenomenon is not peculiar to denominator two at the aggregate level. Equation `(7)` says that every divisor shell reconstructs `G_q` exactly after summing its primitive phases. Denominator two is simply the unique shell where that reconstruction has cardinality one and hence zero conditioning loss.

## 3. Reconstruction conditioning separates major and minor denominator regimes

The triangle inequality applied to `(7)` gives `(10)`. Cauchy--Schwarz also gives

\[
|G_q(X)|^2
\le
\varphi(r)
\sum_{a\bmod r}^{*}|E_{q,r}(a;X)|^2.
\tag{19}
\]

Thus moving to a larger reduced denominator can make each individual additive mode look more oscillatory, but the inverse projection has an unavoidable shell-size cost unless the phases are controlled jointly with additional arithmetic information.

This cleanly separates two regimes.

For `r=X^{o(1)}`, the shell has only `X^{o(1)}` primitive phases. Any fixed-power pointwise or root-mean-square gain strong enough on the complete shell would immediately give a fixed-power bound for the rough zero mode. Such a theorem is not a cheaper substitute for the missing input isolated by `MC-185`--`MC-188`.

For `r=X^{\alpha+o(1)}` with fixed `alpha>0`, a pointwise gain `X^{-delta}` loses `X^{alpha+o(1)}` when the shell is summed, producing `(12)`. A genuinely useful high-denominator route must therefore beat that entropy cost or prove signed cancellation in the shell aggregate itself. But the aggregate is exactly `mu(r)G_q(X)`, so such cancellation must come from a source-side relation not supplied by additive Fourier inversion alone.

This is the additive analogue of the information-budget distinction already seen elsewhere in the line: a well-conditioned re-encoding can preserve a target without explaining it, while a more dispersive encoding can make individual coordinates easier only by spreading the target over more of them.

## 4. Relation to the current primorial frontier

`MC-188` uses the smooth primorial `q_y` to obtain strong residue-class dispersion after the best pretentious character is removed. When that character is principal, the theorem subtracts exactly `G_{q_y}(X)` and leaves the fixed-power zero mode untouched.

`MC-190` proves that translation-invariant linear and Hermitian quadratic operators on the multiplicative unit group are character diagonal. `MC-191` extends the obstruction through the canonical quotient maps between nested primorials and shows that rough Möbius inclusion-exclusion remains sector diagonal.

The additive transform `(3)` does evade the *formal hypothesis* of those no-go theorems: multiplication of residue labels is no longer the diagonalizing symmetry. But `(9)` shows why this does not yet create a useful escape. The prime `2`, already present in every active primorial, turns one nonzero additive frequency into the rough principal coefficient itself. More generally `(5)` identifies the exact divisor shells in which that coefficient is aliased.

Therefore the remaining non-equivariant possibility should be stated more narrowly. A viable mechanism cannot merely replace Dirichlet characters by additive characters and invoke cancellation of nonzero frequencies. It must either:

- control a frequency family that reconstructs `G_{q_y}` with subpower conditioning **without** assuming a bound already equivalent in strength to the rough zero mode; or
- prove an independent arithmetic relation that transfers cancellation from genuinely easier high-denominator/minor-arc data into the low-denominator major-arc aliases.

Neither relation is supplied by finite Fourier analysis itself.

## 5. Prior art and novelty assessment

The identity used in `(13)`--`(15)` is classical Ramanujan-sum theory. Ramanujan introduced these sums in S. Ramanujan, *On certain trigonometrical sums and their applications in the theory of numbers*, Transactions of the Cambridge Philosophical Society 22 (1918), no. 13, 259--276. The standard coprime value `c_r(n)=mu(r)` is immediate from the usual divisor formula for `c_r(n)`. The same source is already retained as a Ramanujan-sum anchor in `research/prime_circle/SOURCES.md`. No novelty is claimed for Ramanujan sums, additive Fourier inversion, or their elementary orthogonality.

Möbius exponential sums are also a classical analytic object. R. C. Baker and G. Harman, *Exponential Sums Formed with the Möbius Function*, Journal of the London Mathematical Society 43 (1991), 193--198, DOI `10.1112/jlms/s2-43.2.193`, is a direct established reference. A recent unconditional result of Byungchul Cha and Dong Han Kim, *Exponential Sums by Irrationality Exponent*, arXiv:2504.06726v2 (18 April 2025), obtains fixed-power bounds for **fixed irrational** phases and explicitly contrasts them with Davenport's classical all-real logarithmic saving. Those results do not provide a bound for `(9)`: the aliasing frequencies here are rational and include the fixed denominator-two phase.

A targeted search over Ramanujan sums, Möbius exponential sums, arithmetic progressions, and additive Fourier formulations found the component identities and a substantial literature on exponential-Möbius cancellation, but no need for a novelty claim arises. The mathematical delta stored here is the exact specialization to the current smooth-primorial residue vector and the resulting **rate obstruction**: the particular additive basis change left open after `MC-190`--`MC-191` contains the unresolved rough zero mode as an explicit nonzero frequency, with the general divisor-shell reconstruction `(5)` quantifying what is spent when that alias is spread over more phases.

## 6. Boundaries and falsification checks

The square-free hypothesis on `q` matters to the clean form `(14)` for every divisor `r|q`; it is automatic for the primorials used by this line. The exact single-frequency identity `(9)` additionally requires `2|q`, again automatic for `q_y` once `y>=2`.

The result does **not** say that every nonzero additive mode is hard, nor that high-denominator exponential-sum estimates are useless. Many individual modes can have substantially more oscillation than `G_q`. It says only that the complete additive representation contains exact low-denominator aliases of the zero mode and that recovering the zero mode from a denominator-`r` shell costs at most and, absent additional structure, naturally up to `varphi(r)` coordinates.

It also does not rule out irrational phases, source-specific bilinear identities, major/minor-arc coupling, nonlinear statistics, or genuinely non-equivariant boundary operators carrying more structure than the additive transform `(3)`. Those remain outside this no-go.

Finally, `(5)` is not an analytic estimate and by itself gives no improvement for `G_q`. Any claimed fixed-power consequence must identify an independently proved bound for the relevant `E_{q,r}` family and include the full `varphi(r)` reconstruction cost. Omitting the denominator-two alias or calling all `h != 0` modes transverse would violate the exact identity `(9)`.

## Consequence

The simplest canonical non-multiplicative harmonic re-encoding of the primorial residue vector is now classified. **Additive Fourier coordinates do mix multiplicative character sectors, but that mixing does not remove the principal obstruction: every divisor-denominator shell reconstructs the rough zero mode, and the parity shell is exactly the zero mode at one nonzero frequency.**

This sharpens the live frontier after `MC-191`. The next useful non-equivariant route must contain a genuinely arithmetic transfer between low-denominator major-arc aliases and independently easier data; a change of Fourier basis alone cannot provide the fixed-power currency missing from `MC-185`--`MC-188`.