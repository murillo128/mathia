# PC-022 — cyclic-cover spectrum has exact-order birth layers, while modular zeta is inherited background

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for treating the inherited modular/Riemann-zeta scattering channel of the full cyclic covers as a prime-specific mechanism. The exact-order spectral decomposition itself is classical cyclic representation theory specialized to the prime-circle cover tower; no novelty claim is made for Artin factorization or character theory.

PC-016 showed that the anchored birth surface at a prime level is exactly a complete cyclic cover of the thrice-punctured sphere. This finding asks the next spectral question: **what part of the cover spectrum is actually new at level `n`, rather than inherited from smaller divisor levels?**

The answer is exact. The full-root cyclic-cover tower has a canonical old/new decomposition indexed by the **exact order of deck characters**. It is the spectral dual of the primitive-root decomposition of the vertices. The same calculation also gives an important negative result: the standard modular scattering channel carrying the classical Riemann-zeta quotient lies entirely in the universal old sector and is therefore not born at prime levels.

## 1. The full-root surfaces form an exact divisor tower

For every `n >= 1`, let

\[
B=\widehat{\mathbb C}\setminus\{0,1,\infty\},
\qquad
Y_n=\widehat{\mathbb C}\setminus\bigl(\{0,\infty\}\cup\mu_n\bigr),
\]

with `Y_1=B`, and let

\[
F_n(z)=z^n.
\]

Then

\[
\boxed{F_n:Y_n\longrightarrow B}
\]

is an unbranched regular cyclic cover of degree `n`, with deck group `C_n` acting by multiplication by `n`-th roots of unity.

More generally, if `d | n`, then

\[
\boxed{z^{n/d}:Y_n\longrightarrow Y_d}
\]

is an unbranched regular cyclic cover of degree `n/d`, because

\[
(z^{n/d})^{-1}(\mu_d)=\mu_n.
\]

Thus the full-root surfaces are not merely a collection of covers of one base: they form a canonical divisor-indexed cover tower.

PC-016 compares this full-root tower with the actual anchored birth surface

\[
X_n^{\rm birth}
=\widehat{\mathbb C}\setminus
\bigl(\{0,1,\infty\}\cup\mu_n^*\bigr),
\]

and proves

\[
X_n^{\rm birth}=Y_n\iff n\text{ is prime}.
\]

The present spectral decomposition is therefore exact on every `Y_n` and applies directly to `X_p^{birth}` when `p` is prime.

## 2. Deck Fourier decomposition gives one universal twisted family

Topologically `B` is the thrice-punctured sphere. Choose the homomorphism

\[
\omega:\pi_1(B)\longrightarrow\mathbb Z
\]

that records winding around `0`: a positively oriented loop around `0` maps to `1`, a loop around `1` maps to `0`, and a loop around `infinity` maps to `-1`.

The cover `Y_n -> B` is the cover associated with

\[
\ker(\omega\bmod n).
\]

For `theta in R/Z`, define the unitary character

\[
\chi_\theta(\gamma)
=\exp\bigl(2\pi i\theta\,\omega(\gamma)\bigr).
\]

Fourier decomposition of the regular representation of `C_n` then gives the exact orthogonal decomposition

\[
\boxed{
L^2(Y_n)
\cong
\bigoplus_{k=0}^{n-1}L^2(B,\chi_{k/n}).
}
\]

Here `L^2(B,chi)` denotes square-integrable sections of the flat line bundle on `B` with holonomy `chi`. The hyperbolic Laplacian respects this decomposition, including the discrete and continuous automorphic spectral problems with the usual cusp-domain conventions.

This already gives a useful restriction: **all full-cover spectra are rational samples of one universal holonomy family `chi_theta` on the fixed base `B`**. Prime denominators do not create a new type of representation by themselves.

## 3. Exact-order characters are the spectral birth layers

A character `chi_{k/n}` has exact order

\[
d=\frac{n}{\gcd(k,n)}.
\]

Every rational `k/n` reduces uniquely to `a/d` with `d | n` and `(a,d)=1`. Define the exact-order spectral layer

\[
\boxed{
\mathcal H_d^{\rm birth}
:=
\bigoplus_{\substack{0\le a<d\\(a,d)=1}}
L^2(B,\chi_{a/d}),
}
\]

with `H_1^{birth}=L^2(B,1)`.

Then

\[
\boxed{
L^2(Y_n)
\cong
\bigoplus_{d\mid n}\mathcal H_d^{\rm birth}.
}
\]

The multiplicity count is exactly

\[
\#\{\text{characters of exact order }d\}=\varphi(d).
\]

This is the spectral analogue of the elementary vertex decomposition

\[
\boxed{
\mu_n=\bigsqcup_{d\mid n}\mu_d^*.
}
\]

So the primitive/new-vertex operation has a canonical dual operation on the cyclic-cover spectral side: retain precisely the deck characters of exact order `n`.

For a prime `p`, there are no intermediate divisors, hence

\[
\boxed{
L^2(X_p^{\rm birth})
=L^2(Y_p)
\cong
\mathcal H_1^{\rm birth}\oplus\mathcal H_p^{\rm birth}.
}
\]

The statement that a prime level has only an old base sector and one new exact-order sector is exact, but it is also ultimately the statement that `C_p` has no nontrivial proper subgroup. It should not be mistaken for an RH mechanism.

## 4. The birth projector itself is a Ramanujan projector

Let `U_j` be the unitary action on `L^2(Y_n)` of the deck transformation `z -> exp(2 pi i j/n) z`. The projector onto the character `k` is

\[
P_k=\frac1n\sum_{j=0}^{n-1}
 e^{-2\pi i kj/n}U_j.
\]

Summing over primitive `k` gives the projector onto the exact-order-`n` spectral birth layer:

\[
\begin{aligned}
P_n^{\rm birth}
&=\sum_{(k,n)=1}P_k\\
&=\frac1n\sum_{j=0}^{n-1}
\left(\sum_{(k,n)=1}e^{-2\pi i kj/n}\right)U_j\\
&=\boxed{
\frac1n\sum_{j=0}^{n-1}c_n(j)U_j
},
\end{aligned}
\]

where `c_n(j)` is the classical Ramanujan sum.

Thus even the algebraic operation that extracts the new spectral sector is not mysterious: it is the same primitive-root Fourier algebra already encountered elsewhere in the prime-circle program. What may still be nontrivial is the **twisted spectral data inside** those exact-order sectors, not the projector selecting them.

## 5. Selberg zeta has the same divisor decomposition

The Venkov–Zograf Artin formalism for finite-index Fuchsian covers applies to the cyclic cover `Y_n -> B`. Since the regular representation of `C_n` is the direct sum of its one-dimensional characters,

\[
\boxed{
Z_{Y_n}(s)
=
\prod_{k=0}^{n-1}Z_B(s,\chi_{k/n}),
}
\]

where `Z_B(s,chi)` is the Selberg zeta function twisted by the corresponding unitary character.

Define the exact-order factor

\[
\boxed{
Z_d^{\rm birth}(s)
:=
\prod_{\substack{0\le a<d\\(a,d)=1}}
Z_B(s,\chi_{a/d}).
}
\]

Then character reduction gives the exact multiplicative divisor decomposition

\[
\boxed{
Z_{Y_n}(s)=\prod_{d\mid n}Z_d^{\rm birth}(s).
}
\]

Consequently multiplicative Möbius inversion gives

\[
\boxed{
Z_n^{\rm birth}(s)
=
\prod_{d\mid n}Z_{Y_d}(s)^{\mu(n/d)}.
}
\]

This identity should be read as an **old/new spectral factorization**, not as a new appearance of the Riemann zeta function. Venkov–Zograf also prove the corresponding Artin formalism for automorphic scattering determinants; the exact matrix/determinant normalization depends on the singular cusp subspaces of each twist, so the operator decomposition above is the safer invariant statement.

For every `n>1`, the trivial-character factor `Z_B(s,1)` is absent from `Z_n^{birth}`. Equivalently, in the Möbius product its total exponent is

\[
\sum_{d\mid n}\mu(n/d)=0.
\]

So the canonical spectral birth extraction **removes**, rather than creates, the universal base factor.

## 6. The classical Riemann-zeta scattering channel is old at every level

The base `B` is the modular curve `Y(2)`, equivalently

\[
B\cong\Gamma(2)\backslash\mathbb H.
\]

The principal congruence subgroup `Gamma(2)` is normal in `PSL_2(Z)` and

\[
PSL_2(\mathbb Z)/\Gamma(2)\cong S_3.
\]

Therefore the `S_3`-invariant subspace of the trivial sector

\[
\mathcal H_1^{\rm birth}=L^2(B)
\]

is exactly the lift of the automorphic spectral problem on the modular surface `PSL_2(Z)\H`.

For the modular Eisenstein series, the scalar scattering coefficient is the classical formula

\[
\boxed{
\phi_{\rm mod}(s)
=
\sqrt\pi\,
\frac{\Gamma(s-\tfrac12)}{\Gamma(s)}
\frac{\zeta(2s-1)}{\zeta(2s)}.
}
\]

Hence a canonical scattering channel whose meromorphic structure contains the nontrivial Riemann zeros is already present inside `H_1^{birth}`.

But `H_1^{birth}` occurs in **every** `Y_n`, independently of whether `n` is prime or composite. At a prime level `X_p^{birth}=Y_p`, the Riemann-zeta-bearing modular channel is therefore inherited unchanged from the base sector; it is not produced by the primitive `p`-shell.

Moreover, the exact-order birth extraction for every `n>1` discards the entire trivial sector. Thus the natural old/new spectral decomposition gives a decisive interpretation rule:

\[
\boxed{
\text{Riemann zeros seen through the inherited modular scattering channel}
\neq
\text{prime-circle spectral mechanism}.
}
\]

They are universal background already present before the level-`n` spectral birth layer is added.

This does **not** prove that the exact-order twisted sectors are unrelated to Riemann or Dirichlet `L`-functions. It proves only that the familiar modular/Riemann-zeta scattering factor cannot be counted as evidence for a mechanism generated by prime-circle birth geometry.

## 7. Relation to PC-016 through PC-021

This finding materially sharpens the spectral promise in PC-016.

- PC-016 supplied the exact cover criterion `X_p^{birth}=Y_p` at prime levels.
- PC-017 showed that composite birth surfaces differ from the full covers by a canonical nonlinear uniformization/accessory defect.
- PC-018 ruled out factor-order holonomy of those first-difference defects.
- PC-021 ruled out regular fixed linear probes as sources of a new reciprocal-zeta mechanism.
- PC-022 now shows that the **linear automorphic spectrum of the full cyclic-cover tower has its own exact old/new decomposition**, and that the most obvious Riemann-zeta scattering channel belongs entirely to the old base sector.

The surviving spectral question is therefore narrower than “do Riemann zeros occur somewhere in the prime-level cover spectrum?” They already occur in inherited modular background. A substantive continuation must instead establish one of the following:

1. a forced, non-generic relation between the exact-order twisted family `H_n^{birth}` and the critical-line problem that is not just rational-character/Ramanujan algebra; or
2. a relation arising from the nonlinear difference between the actual composite birth surface and the full-root cover, i.e. the uniformization/accessory sector of PC-017.

## 8. Prior art and novelty audit

The relevant mathematical ingredients are classical:

- cyclic-cover spectral decomposition into deck-character sectors is standard finite-cover/representation theory;
- Venkov and Zograf proved Artin factorization formulas for Selberg zeta functions and automorphic scattering determinants for finite-index subgroups of Fuchsian groups;
- `B = P^1 - {0,1,infinity}` as `Gamma(2)\H`, the quotient `PSL_2(Z)/Gamma(2) = S_3`, and the modular Eisenstein scattering coefficient are standard modular-form theory;
- grouping cyclic characters by exact order and obtaining Ramanujan sums in the corresponding group-algebra projector is elementary finite Fourier analysis.

No historical novelty is claimed for any of these ingredients or for Artin formalism. The durable prime-circle contribution is the **exact organization and the negative research consequence**: vertex birth under divisor decomposition has a matching spectral exact-order decomposition, and this decomposition classifies the familiar Riemann-zeta scattering channel as inherited old background rather than level-born evidence.

Primary/standard anchors used here are A. B. Venkov and P. G. Zograf, *On analogues of the Artin factorization formulas in the spectral theory of automorphic functions connected with induced representations of Fuchsian groups* (Math. USSR-Izv. 21 (1983), 435–443, DOI 10.1070/IM1983v021n03ABEH001800), and standard modular Eisenstein/scattering theory as presented for example in H. Iwaniec, *Spectral Methods of Automorphic Forms*, 2nd ed. (AMS, 2002).

## 9. Audit boundary and falsification tests

The exact claims can be independently checked without numerical fitting:

1. verify that the monodromy of `z^n:Y_n->B` is `omega mod n`;
2. decompose the regular representation of `C_n` and group characters by exact order, recovering `sum_{d|n} phi(d)=n`;
3. compute the exact-order projector and recover the Ramanujan coefficients `c_n(j)/n`;
4. apply the Venkov–Zograf finite-index factorization to the normal cyclic subgroup corresponding to `Y_n`;
5. identify the `S_3`-invariant part of the trivial `Gamma(2)` sector with the modular surface and recover the classical modular scattering coefficient.

Failure of any one of these exact identifications would invalidate the corresponding part of the finding. No claim is made here that the new twisted sectors solve RH, that their poles equal Riemann zeros, or that the exact-order packaging is historically new.
