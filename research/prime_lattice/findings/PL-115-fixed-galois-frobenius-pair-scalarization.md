# PL-115 — Fixed Galois Frobenius pair geometry scalarizes to Artin character channels

## Claim

`PL-114` shows that fixed congruence labels at a fixed modulus do not preserve an irreducible two-prime geometry: finite Fourier analysis reduces them to finitely many Dirichlet-character prime channels. A natural attempted escape is to replace the finite abelian residue group by genuinely nonabelian Galois data. For one fixed finite Galois extension this also fails, for a structural reason that is stronger than the abelian calculation.

Let `L/Q` be a fixed finite Galois extension with group `G`, let `S` be the finite set of ramified rational primes, and write `C_p` for the Frobenius **conjugacy class** of an unramified prime `p`. Fix an exponent depth `l>=1` and a symmetric kernel

`W : G^sharp x G^sharp -> C`,

where `G^sharp` is the finite set of conjugacy classes. Define

`C_{l,L,W}(n)
 = sum_{p<q, p,q notin S,
        v_p(n)>=l, v_q(n)>=l}
     W(C_p,C_q)`.

Then for `Re(s)>1`,

`F_{l,L,W}(s)
 := sum_{n>=1} C_{l,L,W}(n)n^(-s)
  = zeta(s) Q_{L,W}(l s)`,

with

`Q_{L,W}(a)
 = sum_{p<q, p,q notin S} W(C_p,C_q)(pq)^(-a)`.

Because `G^sharp` is finite, `Q_{L,W}` is exactly a finite bilinear form in the scalar Frobenius-class prime sums

`P_C(a)=sum_{p notin S, C_p=C} p^(-a)`.

Moreover irreducible characters form an orthonormal basis of class functions on `G`. Consequently every `P_C` is a finite linear combination of the scalar character prime sums

`P_chi(a)=sum_{p notin S} chi(C_p)p^(-a)`,

and hence every fixed `Q_{L,W}` is a finite bilinear combination of `P_chi(a)` together with finite diagonal terms at `2a`.

The nonabelian group therefore does **not** supply canonical matrix-valued prime-pair geometry at this level. A rational prime determines `Frob_p` only up to conjugacy. Choosing a matrix `rho(Frob_p)` in a representation introduces a prime-by-prime conjugation gauge; there is no canonical relative frame in which matrices attached to two different rational primes can be multiplied or compared. Prime-wise canonical data are conjugacy invariants, and fixed conjugacy-invariant data are exhausted by the finite character basis. The resulting scalar channels are classical Artin-L/Frobenian data.

Thus the route

`fixed finite nonabelian Galois label + fixed-depth pair kernel -> canonical matrix-valued RH geometry`

is obstructed. Nonabelianity alone does not evade the finite-label scalarization found in `PL-114`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for fixed finite Galois extensions, fixed exponent depth, and pair observables depending canonically only on the individual Frobenius conjugacy classes. No novelty is claimed for Chebotarev/Frobenian functions, finite-group character Fourier analysis, Artin L-functions, or Frobenian Euler-product factorization. The durable contribution is the line-specific no-go: the most canonical nonabelian finite-label repair to `PL-114` loses its apparent matrix freedom before any critical-line mechanism appears.

## 1. Exact exponent-lattice factorization

For distinct unramified primes `p,q`, the two depth conditions are exactly

`v_p(n)>=l, v_q(n)>=l
 <=> (pq)^l | n`.

Hence, for `sigma=Re(s)>1`, absolute convergence permits the order of summation to be exchanged and gives

`sum_{n:(pq)^l|n} n^(-s)
 = (pq)^(-l s) zeta(s)`.

Therefore

`F_{l,L,W}(s)
 = zeta(s)
   sum_{p<q, p,q notin S}
     W(C_p,C_q)(pq)^(-l s)`.

No Chebotarev theorem, Euler product, or analytic continuation is needed for this identity. The Galois input enters only in the label assigned to each prime coordinate; the exponent-lattice incidence is the same principal-ideal calculation as in `PL-112`--`PL-114`.

Now group the primes by Frobenius conjugacy class. For `Re(a)>1`, define

`P_C(a)=sum_{p notin S, C_p=C} p^(-a)`.

Ordered-pair symmetrization gives the exact finite-class formula

`Q_{L,W}(a)
 = 1/2 [
     sum_{C,D in G^sharp}
       W(C,D) P_C(a)P_D(a)
     - sum_{C in G^sharp}
       W(C,C) P_C(2a)
   ]`.

The second term removes `p=q`. This already proves finite scalarization: no matter how nonabelian `G` is, a fixed pair kernel on its finitely many conjugacy classes has no infinite-dimensional pair incidence left after the class aggregation.

## 2. Irreducible characters exhaust the canonical fixed-group channels

Let `Irr(G)` denote the irreducible complex characters. For a class `C`, character orthogonality gives

`1_C(g)
 = (|C|/|G|)
   sum_{chi in Irr(G)}
     overline(chi(C)) chi(g)`.

Summing this identity over unramified primes with weight `p^(-a)` yields

`P_C(a)
 = (|C|/|G|)
   sum_{chi in Irr(G)}
     overline(chi(C)) P_chi(a)`,

where

`P_chi(a)=sum_{p notin S} chi(C_p)p^(-a)`.

Thus `Q_{L,W}` is a finite bilinear form in the vector `(P_chi(a))_{chi in Irr(G)}`. Equivalently, expand the two-variable class function `W` in the tensor character basis,

`W(g,h)=sum_{chi,psi} c_{chi,psi} chi(g)psi(h)`.

Then the ordered pair sum becomes a finite combination of

`P_chi(a)P_psi(a)`

and the diagonal correction is a finite combination of

`P_{chi psi}(2a)`,

where `chi psi` is the character of the tensor-product representation and may be decomposed again into irreducibles.

This is the nonabelian analogue of the Dirichlet-character diagonalization in `PL-114`, but with an important difference in interpretation: irreducible representations can have dimension greater than one, yet the **canonical prime data remain scalar characters** because the Frobenius label itself is only a conjugacy class.

## 3. Why raw representation matrices are not a canonical escape

Suppose `rho:G->GL(V)` is a nonabelian representation. For an unramified rational prime `p`, choosing a prime of `L` above `p` selects a Frobenius element `g_p`, but another choice replaces it by

`g_p -> h_p g_p h_p^(-1)`.

Consequently

`rho(g_p) -> rho(h_p) rho(g_p) rho(h_p)^(-1)`.

The conjugating element can be chosen independently at different rational primes. A putative pair observable such as a matrix entry of `rho(g_p)`, or a product comparing `rho(g_p)` and `rho(g_q)` in a fixed basis, is therefore not intrinsically attached to the pair `(p,q)`. A trace such as `tr rho(g_p)=chi(C_p)`, the characteristic polynomial of `rho(g_p)`, or any other individual conjugacy invariant is canonical, but it has already descended to a class function and hence to the finite scalar character decomposition above.

This is a gauge obstruction, not merely a dimension count. Nonabelian representation theory supplies matrix spaces, but the ordinary rational-prime Frobenius data do not supply a canonical relative trivialization between those spaces at different primes. To retain genuine matrix coupling one must add extra transport, a globally specified representation-theoretic target, compatible local frames, or another structure that is **not** contained in the unordered collection of Frobenius conjugacy classes. Such additions lie outside this finding and must justify their own canonicity.

## 4. Artin L-functions are the classical scalar continuation channels

For a representation with character `chi`, remove the finite ramified set `S` and write the partial Artin L-function

`L^S(s,chi)
 = product_{p notin S}
     det(I-rho(Frob_p)p^(-s))^(-1)`

in its absolutely convergent half-plane. Taking logarithms there gives

`log L^S(s,chi)
 = sum_{r>=1} (1/r)
     P_{psi^r chi}(r s)`,

where the Adams operation on characters is

`(psi^r chi)(g)=chi(g^r)`.

The Adams operation is a virtual-character operation in the representation ring. Ordinary Möbius inversion in the power index therefore gives, still initially only in the absolute-convergence half-plane,

`P_chi(s)
 = sum_{r>=1} mu(r)/r
     log L^S(r s, psi^r chi)`.

Indeed, after substituting the previous logarithmic expansion, the coefficient of `P_{psi^n chi}(n s)` is

`(1/n) sum_{r|n} mu(r)`,

which vanishes unless `n=1`.

This identifies the scalar channels produced by the lattice pair observable with standard Artin-L data. Brauer induction supplies meromorphic continuation of Artin L-functions; Artin holomorphy for nontrivial irreducibles is **not** assumed here. The displayed logarithmic inversion must accordingly be interpreted branchwise away from inherited zeros and poles. It does not turn `P_chi` into a globally single-valued meromorphic function, nor does it yield a new zero-location law.

This classicalization is consistent with the broader Frobenian literature. Frobenian functions are precisely functions of primes determined by Frobenius conjugacy data; irreducible characters are the finite Fourier basis for class functions, and Artin L-functions are the corresponding analytic channels. Recent expositions of Frobenian Euler-product factorization make this reduction explicit even for genuinely nonabelian examples.

## 5. Critical-strip boundary and what actually survives

The pair factor itself has the direct absolutely convergent series

`Q_{L,W}(a)
 = sum_{p<q, p,q notin S}
     W(C_p,C_q)(pq)^(-a)`,

so it is holomorphic for `Re(a)>1`. Hence

`zeta(s) Q_{L,W}(l s)`

continues the original lattice Dirichlet series meromorphically to

`Re(s)>1/l`,

using only the standard continuation of `zeta(s)` and the directly convergent pair factor. No continuation of an Euler product or of the Artin prime sums is needed for this window.

The same depth boundary found in `PL-113`--`PL-114` therefore remains:

- at `l=1`, the pair factor does not enter the critical strip;
- at `l=2`, `Re(s)=1/2` is the elementary absolute-convergence boundary of the pair factor;
- at `l>=3`, the pair factor is already holomorphic across `Re(s)=1/2`, and ordinary Riemann zeros enter the continued transform through the explicit scalar factor `zeta(s)`, subject only to possible accidental cancellation by `Q`.

The nonabelian Galois labels do not change this geometry. If one analytically continues the Frobenius character prime sums farther left, their singular input is inherited from Artin L-functions and therefore broadens the scalar divisor under study; it does not produce a mechanism forcing the Riemann divisor onto its critical line.

## 6. Prior-art and novelty audit

The closest structural prior art is classical and modern work on Frobenian functions, finite-group character Fourier analysis, and Artin L-functions.

- **Daniel Fiorilli and Florent Jouve**, “Distribution of Frobenius elements in families of Galois extensions,” *Journal of the Institute of Mathematics of Jussieu* **23**(3) (2024), 1169–1258, DOI `10.1017/S1474748023000154`. Their setup explicitly treats Frobenius as conjugacy-class data, takes class functions on a finite Galois group, Fourier-expands them against irreducible characters, and connects the resulting prime-counting observables to Artin L-functions.
- **Mark D. Coleman**, “The Hooley-Huxley contour method for problems in number fields III: frobenian functions,” *Journal de Théorie des Nombres de Bordeaux* **13**(1) (2001), 65–76, DOI `10.5802/jtnb.304`. This is direct prior art for arithmetic functions whose prime values depend only on Frobenius class.
- **Brandon Alberts**, “Explicit analytic continuation of Euler products,” *Essential Number Theory* **5**(1) (2026), 49–112, DOI `10.2140/ent.2026.5.49`, arXiv `2406.18190`. Its Frobenian factorization discussion explicitly uses irreducible characters as a basis for class functions and Artin L-factors for nonabelian Frobenius coefficients, including higher-dimensional representations.

Accordingly, neither Frobenius labeling, character decomposition, nor the Artin-L bridge is Mathia novelty. The exact exponent-depth pair observable above was not located as a named theorem, but that is not used as a novelty claim. Its durable value is as a **route classification** relative to `PL-114`: replacing fixed abelian congruence labels by fixed nonabelian Galois labels does not by itself restore matrix-valued arithmetic geometry, because canonicity forces descent to conjugacy classes and finite scalar character channels.

## Adversarial boundaries

1. **The Galois extension is fixed.** A tower whose degree, conductor, or group complexity grows with the observation scale can carry an unbounded number of character channels and is not controlled uniformly by this finite-dimensional reduction.
2. **The observable uses the individual Frobenius conjugacy classes.** A genuinely global object supplying coherent transport between local representation spaces could make matrix comparisons canonical and lies outside the result.
3. **Ramified primes are excluded only to keep the statement clean.** They form a finite set for fixed `L/Q`; restoring their inertia-dependent local factors produces finite corrections and cannot restore an infinite-prime matrix coupling.
4. **Character scalarization is not triviality.** Artin L-functions contain deep arithmetic information. The negative statement is that the proposed prime-pair geometry has already collapsed to classical scalar channels before that information is analyzed.
5. **No Artin conjecture is assumed.** Meromorphic continuation from Brauer induction is enough for the provenance statement; branch singularities of `log L` must not be mistaken for a globally meromorphic prime sum.
6. **No statement about arbitrary arithmetic pair relations is made.** Prime gaps, additive equations, varying Galois extensions, l-adic representations with additional global structure, or target-relative operators remain outside the no-go.
7. **The fixed finite-label matched control still applies.** Once only the finite class label `C_p` is retained, the bilinear reduction works for any free multiplicative system with generators carrying labels in a fixed finite set. The specifically arithmetic content is in which labels rational primes receive and in the resulting scalar Artin channels, not in the finite pair geometry itself.

## Consequence for the research line

`PL-114` left open the possibility that a genuinely arithmetic pair relation might evade the finite abelian congruence calculation. A fixed nonabelian Galois extension is the cheapest canonical test because it enriches each prime by real arithmetic local data and offers higher-dimensional representations. The test is nevertheless negative:

`prime coordinate -> Frobenius conjugacy class -> finite class-function Fourier transform -> scalar Artin character channels`.

The apparent matrix freedom disappears at the first arrow where canonicity is enforced. A viable Galois/local-global continuation of the prime-lattice program must therefore add something not present in one fixed set of prime-wise conjugacy classes: scale-growing Galois complexity, a canonical transport/coupling between local representation spaces, a target-relative operator, or another global structure that cannot be reduced to finitely many scalar Artin channels.

This does not close Galois or adelic approaches. It closes the tempting inference that **nonabelian finite local labels themselves** provide the missing multidimensional RH rigidity.