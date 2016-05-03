# Algorithms and Data Structures: Hash Tables & Hashing
# 4.26.2016
# @totallygloria


import sys
import unittest
from StringIO import StringIO
from HashTableOAClass import OAHashTable

# [5, 7, 13, 19, 31, 43, 61, 73, 103, 109, 139, 151, 181, 193, 199, 229, 241, 271, 283, 313, 349, 421, 433, 463, 523, 571, 601, 619, 643, 661, 811, 823, 829, 859, 883, 1021, 1033, 1051, 1063, 1093, 1153, 1231, 1279, 1291, 1303, 1321, 1429, 1453, 1483, 1489, 1609, 1621, 1669, 1699, 1723, 1789, 1873, 1879, 1933, 1951, 1999, 2029, 2083, 2089, 2113, 2131, 2143, 2239, 2269, 2311, 2341, 2383, 2551, 2593, 2659, 2689, 2713, 2731, 2791, 2803, 2971, 3001, 3121, 3169, 3253, 3259, 3301, 3331, 3361, 3373, 3391, 3463, 3469, 3529, 3541, 3559, 3583, 3673, 3769, 3823, 3853, 3919, 3931, 4003, 4021, 4051, 4093, 4129, 4159, 4219, 4231, 4243, 4261, 4273, 4339, 4423, 4483, 4519, 4549, 4639, 4651, 4723, 4789, 4801, 4933, 4969, 5011, 5023, 5101, 5233, 5281, 5419, 5443, 5479, 5503, 5521, 5641, 5653, 5659, 5743, 5851, 5869, 5881, 6091, 6133, 6199, 6271, 6301, 6361, 6451, 6553, 6571, 6661, 6691, 6703, 6763, 6781, 6793, 6829, 6871, 6949, 6961, 7129, 7213, 7309, 7333, 7351, 7459, 7489, 7549, 7561, 7591, 7759, 7879, 7951, 8011, 8089, 8221, 8233, 8293, 8389, 8431, 8539, 8599, 8629, 8821, 8839, 8863, 8971, 9001, 9013, 9043, 9241, 9283, 9343, 9421, 9433, 9439, 9463, 9631, 9679, 9721, 9769, 9859, 9931, 10009, 10039, 10069, 10093, 10141, 10273, 10303, 10333, 10429, 10459, 10501, 10531, 10711, 10861, 10891, 10939, 11059, 11071, 11119, 11161, 11173, 11353, 11491, 11551, 11701, 11719, 11779, 11833, 11941, 11971, 12043, 12073, 12109, 12163, 12241, 12253, 12379, 12541, 12613, 12823, 12919, 13003, 13009, 13219, 13339, 13399, 13681, 13693, 13711, 13723, 13759, 13831, 13879, 13903, 13933, 13999, 14011, 14083, 14251, 14323, 14389, 14449, 14551, 14563, 14593, 14629, 14869, 15139, 15271, 15289, 15331, 15361, 15583, 15643, 15649, 15733, 15739, 15889, 15973, 16063, 16069, 16141, 16189, 16231, 16363, 16453, 16633, 16651, 16693, 16831, 16903, 16981, 17029, 17191, 17209, 17293, 17389, 17419, 17491, 17581, 17599, 17659, 17683, 17749, 17791, 17839, 17911, 17923, 17959, 17989, 18043, 18049, 18061, 18121, 18133, 18253, 18289, 18313, 18523, 18541, 18913, 18919, 19081, 19141, 19183, 19213, 19381, 19423, 19429, 19471, 19543, 19699, 19753, 19843, 19891, 19963, 19993, 20023, 20149, 20233, 20359, 20443, 20479, 20509, 20551, 20641, 20719, 20749, 20773, 20809, 20899, 20983, 21013, 21019, 21061, 21193, 21319, 21379, 21493, 21523, 21559, 21589, 21601, 21613, 21649, 21739, 21841, 22039, 22093, 22111, 22159, 22273, 22279, 22369, 22483, 22543, 22573, 22621, 22639, 22699, 22741, 22861, 22963, 23029, 23041, 23059, 23203, 23293, 23371, 23539, 23563, 23629, 23671, 23689, 23743, 23833, 23911, 24109, 24181, 24373, 24421, 24919, 24979, 25033, 25171, 25303, 25309, 25411, 25471, 25579, 25603, 25801, 25849, 25933, 25999, 26113, 26251, 26263, 26683, 26701, 26713, 26731, 26863, 26881, 26893, 26953, 27061, 27109, 27241, 27283, 27409, 27481, 27529, 27541, 27583, 27691, 27739, 27751, 27793, 27919, 27943, 28099, 28111, 28183, 28279, 28309, 28351, 28411, 28549, 28573, 28621, 28663, 28753, 29023, 29131, 29209, 29389, 29401, 29569, 29671, 29761, 29881, 30013, 30091, 30139, 30271, 30391, 30469, 30493, 30559, 30841, 30853, 30871, 31081, 31123, 31153, 31183, 31249, 31321, 31393, 31513, 31543, 31723, 31729, 31771, 31849, 32029, 32059, 32119, 32143, 32191, 32299, 32323, 32371, 32413, 32443, 32533, 32563, 32611, 32719, 32803, 32833, 32911, 32941, 32971, 33073, 33151, 33181, 33289, 33331, 33349, 33589, 33601, 33619, 33751, 33769, 33811, 33829, 34033, 34129, 34159, 34213, 34261, 34303, 34369, 34471, 34501, 34513, 34591, 34651, 34759, 34843, 34849, 34963, 35053, 35083, 35281, 35449, 35509, 35533, 35593, 35731, 35803, 35839, 35899, 36013, 36109, 36343, 36469, 36529, 36781, 36793, 36901, 36931, 37021, 37201, 37309, 37339, 37363, 37549, 37573, 37591, 37693, 37783, 37813, 37993, 38239, 38329, 38449, 38461, 38569, 38611, 38653, 38671, 38713, 38749, 38923, 39043, 39163, 39229, 39241, 39343, 39373, 39511, 39829, 39841, 40039, 40129, 40153, 40429, 40531, 40639, 40699, 40849, 41143, 41179, 41203, 41233, 41389, 41413, 41521, 41611, 41761, 41851, 41959, 41983, 42019, 42073, 42181, 42223, 42283, 42409, 42463, 42571, 42643, 42703, 42841, 42901, 43051, 43321, 43399, 43543, 43579, 43609, 43651, 43783, 43789, 43891, 43963, 44029, 44089, 44131, 44203, 44269, 44281, 44383, 44533, 44623, 44701, 44773, 45121, 45139, 45181, 45319, 45343, 45589, 45823, 46051, 46093, 46183, 46273, 46309, 46351, 46441, 46591, 46681, 46771, 46819, 46831, 47059, 47149, 47353, 47389, 47419, 47659, 47701, 47713, 47743, 47779, 47809, 48121, 48313, 48409, 48481, 48541, 48649, 48679, 48733, 48781, 48823, 48859, 48871, 48991, 49033, 49123, 49171, 49201, 49279, 49333, 49369, 49393, 49411, 49531, 49549, 49669, 49741, 49789, 49921, 49939, 49993, 50023, 50053, 50131, 50263, 50461, 50551, 50593, 50893, 50971, 51061, 51133, 51199, 51241, 51343, 51349, 51421, 51439, 51481, 51721, 51769, 51829, 51871, 51973, 52069, 52183, 52291, 52363, 52543, 52711, 52861, 52903, 53089, 53149, 53173, 53233, 53269, 53281, 53551, 53593, 53611, 53719, 53899, 54013, 54403, 54421, 54499, 54541, 54583, 54631, 54919, 55051, 55219, 55333, 55339, 55441, 55621, 55633, 55663, 55819, 55903, 55933, 56041, 56101, 56209, 56239, 56269, 56479, 56503, 56533, 56599, 56713, 56809, 56893, 56911, 56923, 57193, 57223, 57271, 57331, 57349, 57529, 57559, 57793, 57901, 58111, 58153, 58171, 58231, 58369, 58393, 58441, 58453, 58603, 58789, 58909, 59011, 59023, 59053, 59209, 59221, 59359, 59419, 59443, 59473, 59629, 59671, 60091, 60103, 60169, 60259, 60649, 60661, 60763, 60889, 60901, 60919, 61153, 61333, 61381, 61471, 61561, 61981, 62131, 62143, 62191, 62299, 62929, 62971, 62983, 62989, 63031, 63199, 63313, 63391, 63421, 63589, 63601, 63649, 63691, 63841, 64153, 64189, 64303, 64453, 64579, 64663, 64783, 64879, 64921, 65029, 65101, 65173, 65269, 65449, 65521, 65539, 65581, 65701, 65719, 65731, 65839, 65929, 65983, 66109, 66361, 66571, 66751, 66853, 66949, 67141, 67189, 67213, 67219, 67273, 67411, 67429, 67579, 67759, 67933, 68113, 68209, 68281, 68449, 68491, 68713, 68821, 68881, 68899, 69031, 69151, 69193, 69259, 69403, 69493, 69499, 69739, 69763, 69829, 69859, 69931, 70003, 70123, 70141, 70183, 70201, 70381, 70459, 70489, 70573, 70621, 70843, 70879, 70921, 70951, 70981, 70999, 71263, 71329, 71341, 71389, 71413, 71473, 71551, 71713, 71809, 71881, 72091, 72103, 72169, 72223, 72229, 72253, 72271, 72469, 72649, 72673, 72871, 73039, 73063, 73363, 73609, 73681, 73849, 74101, 74161, 74203, 74383, 74413, 74509, 74611, 74719, 74731, 74761, 75013, 75169, 75211, 75391, 75403, 75541, 75619, 75709, 75991, 76003, 76081, 76159, 76261, 76369, 76423, 76543, 76651, 76831, 76873, 76963, 77239, 77263, 77269, 77419, 77479, 77491, 77551, 77689, 77713, 78139, 78193, 78439, 78511, 78541, 78571, 78781, 78889, 78979, 79153, 79231, 79399, 79561, 79633, 79693, 79699, 79813, 79843, 79903, 79999, 80149, 80209, 80233, 80449, 80473, 80491, 80629, 80671, 80683, 80749, 80779, 80833, 80911, 81019, 81043, 81049, 81199, 81283, 81373, 81553, 81649, 81703, 81901, 81931, 81973, 82009, 82039, 82141, 82219, 82351, 82471, 82531, 82561, 82723, 82729, 82759, 82813, 82891, 83221, 83233, 83269, 83341, 83401, 83563, 83641, 83719, 84061, 84181, 84223, 84319, 84349, 84391, 84523, 84631, 84811, 84859, 84871, 84979, 85093, 85201, 85333, 85363, 85429, 85453, 85621, 85669, 85819, 85831, 85933, 86029, 86113, 86293, 86353, 86371, 86533, 86629, 86929, 87013, 87121, 87151, 87181, 87223, 87253, 87511, 87541, 87559, 87589, 87631, 87643, 87721, 87961, 88003, 88261, 88339, 88471, 88591, 88609, 88663, 88801, 88813, 88819, 89071, 89521, 89563, 89599, 89659, 89671, 89821, 89899, 90019, 90073, 90199, 90373, 90403, 90439, 90529, 90619, 90679, 90823, 91081, 91099, 91129, 91141, 91153, 91369, 91459, 91573, 91813, 91969, 92179, 92221, 92383, 92401, 92461, 92569, 92641, 92671, 92683, 92791, 92863, 92959, 93133, 93241, 93253, 93283, 93481, 93493, 93559, 93703, 93763, 93811, 93889, 93913, 94009, 94111, 94153, 94309, 94351, 94399, 94441, 94531, 94543, 94561, 94651, 94849, 94951, 95089, 95191, 95233, 95443, 95791, 95803, 95959, 95989, 96181, 96223, 96331, 96589, 96739, 96799, 96823, 97003, 97159, 97171, 97303, 97369, 97381, 97501, 97549, 97579, 97609, 97651, 97789, 97843, 97849, 97861, 98011, 98299, 98323, 98389, 98563, 98641, 98713, 98731, 98809, 98869, 98899, 98911, 98929, 99133, 99139, 99259, 99349, 99529, 99709, 99721, 99991, 100153, 100363, 100393, 100519, 100549, 100801, 101113, 101119, 101161, 101209, 101281, 101503, 101533, 101749, 101839, 102001, 102061, 102079, 102103, 102199, 102253, 102301, 102409, 102499, 102679, 102763, 102913, 102931, 103069, 103093, 103291, 103393, 103423, 103813, 103843, 103969, 103981, 103993, 104089, 104149, 104233, 104311, 104383, 104473, 104551, 104683]


class HashTableOAClassTester(unittest.TestCase):

    def test_create_table(self):
        # Test with 0 as input
        test_input = StringIO(0)
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        self.assertEqual(ht.size, 5)
        # Test with random numbers
        test_input = StringIO(600)
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        self.assertEqual(ht.size, 601)
        test_input = StringIO(1000)
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        self.assertEqual(ht.size, 1021)
        # Test with larger than allowed size
        test_input = StringIO(1000000)
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        self.assertEqual(ht.size, 104683)
        # Test with invalid input, table defaults to 13 slots
        test_input = StringIO("a large number")
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        self.assertEqual(ht.size, 5)

    def test_compute_hash(self):
        test_input = StringIO(1000)  # Create a ht with 1021 slots
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        self.assertEqual(ht.size, 1021)
        self.assertEqual(ht.compute_hash(650), 827)
        self.assertEqual(ht.compute_hash(1024), 9)
        self.assertEqual(ht.compute_hash(123456789), 207)

    def test_insert_hash(self):
        test_input = StringIO(1000)  # Create a ht with 1021 slots
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        # Basic insertion _appears_ to work for immutable types (doesn't duplicate)
        # Numbers, strings, and sets: OK!  Lists & Dicts: Not hashable!
        self.assertEqual(ht.size, 1021)
        ht.insert(650, "item")
        self.assertEqual(ht.occupancy, 1)
        ht.insert(650, "item")
        self.assertEqual(ht.occupancy, 1)
        ht.insert(650.000, "floats aren't ints!")
        self.assertEqual(ht.occupancy, 2)
        ht.insert(65, "different item")
        self.assertEqual(ht.occupancy, 3)
        ht.insert("cat", "can it hash strings? yup!")
        self.assertEqual(ht.occupancy, 4)
        testset = (1,2,3)
        ht.insert(testset, "can it hash sets? yup!")
        self.assertEqual(ht.occupancy, 5)

    def test_membership(self):
        test_input = StringIO(1000)  # Create a ht with 1021 slots
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        # Cause two intentional collisions, makes sure everything is still added
        ht.insert(1, "item")
        self.assertTrue(1 in ht)
        ht.insert(1022, "stuff")
        self.assertTrue(1022 in ht)
        ht.insert(1023, "stuff")
        self.assertEqual(ht.occupancy, 3)
        self.assertTrue(1023 in ht)
        self.assertFalse(2 in ht)

    def test_remove_item(self):
        test_input = StringIO(1000)  # Create a ht with 1021 slots
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        # Intentionally cause two collisions
        ht.insert(1, "item")
        ht.insert(1022, "stuff")
        ht.insert(1023, "things")
        # Remove an item, make sure it's gone and the occupancy is smaller
        self.assertTrue(ht.remove_item(1022))
        self.assertFalse(1022 in ht)
        self.assertEqual(ht.occupancy, 2)
        # Same as above
        self.assertTrue(ht.remove_item(1))
        self.assertFalse(1 in ht)
        self.assertEqual(ht.occupancy, 1)
        ht.insert(2014, "widget")
        self.assertTrue(2014 in ht)
        self.assertEqual(ht.occupancy, 2)
        self.assertTrue(ht.remove_item(2014))
        self.assertFalse(2014 in ht)
        self.assertEqual(ht.occupancy, 1)
        # Check that duplicates don't insert
        ht.insert(1023, "things")
        self.assertTrue(1023 in ht)
        self.assertEqual(ht.occupancy, 1)
        # Check the used spots can take items
        ht.insert(1022, "something else")
        self.assertTrue(1022 in ht)
        self.assertEqual(ht.occupancy, 2)
        # Check if the hash can find non-number entries
        ht.insert(650.000, "floats aren't ints!")
        self.assertTrue(650.000 in ht)
        ht.insert("cat", "can it hash strings? yup!")
        self.assertTrue("cat" in ht)
        testset = (1,2,3)
        ht.insert(testset, "can it hash sets? yup!")
        self.assertTrue(testset in ht)

    def test_resize_table(self):
        test_input = StringIO(13)
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        self.assertTrue(ht.size, 13)
        self.assertEqual(ht.occupancy, 0)
        # Fill table to maximum capacity before resizing (12/13, triggers on #13)
        ht.insert(0, 'a'), ht.insert(1, 'b'), ht.insert(2, 'c')
        ht.insert(3, 'd'), ht.insert(4, 'e')
        self.assertEqual(ht.size, 13)
        self.assertEqual(ht.occupancy, 5)
        ht.insert(5, 'f'), ht.insert(6, 'g'), ht.insert(7, 'h')
        ht.insert(8, 'i'), ht.insert(9, 'j')
        self.assertEqual(ht.size, 13)
        self.assertEqual(ht.occupancy, 10)
        # At this point, the table should be at 0.769 % full and resize up.
        # 2 x 13 = 26, next largest prime is 31
        ht.insert(10, 'k')
        self.assertEqual(ht.size, 31)
        self.assertEqual(ht.occupancy, 11)
        # The next full point for a table of 31 should happen at 22 elements.
        # Trying to insert the 23rd should cause a resize to 73. (Started at 0, i=21)
        for i in range(11,22):
            ht.insert(i, i + 10)
        self.assertEqual(ht.size, 31)
        self.assertEqual(ht.occupancy, 22)
        ht.insert(22, "stuff")
        self.assertEqual(ht.size, 73)
        self.assertEqual(ht.occupancy, 23)
        # The next full point for a table of 73 should happen at 52 elements.
        # Trying to insert the 53rd should cause a resize to 151.
        for i in range(23,52):
            ht.insert(i, i + 20)
        self.assertEqual(ht.size, 73)
        self.assertEqual(ht.occupancy, 52)
        ht.insert(52, "other thing")
        self.assertEqual(ht.size, 151)
        self.assertEqual(ht.occupancy, 53)

    def test_items(self):
        test_input = StringIO(30)
        sys.stdin = test_input
        sys.stdout = StringIO()
        ht = OAHashTable()
        self.assertTrue(ht.size, 31)
        self.assertEqual(ht.occupancy, 0)
        for i in range(5,26):
            ht.insert(i, i + 10)
        self.assertEqual(ht.size, 31)
        self.assertEqual(ht.occupancy, 21)


if __name__ == '__main__':
    unittest.main()
